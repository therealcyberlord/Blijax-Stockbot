# --- Imports --- #
import os
from dotenv import load_dotenv

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.utilities import SerpAPIWrapper

from langchain.agents import load_tools

from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, create_pandas_dataframe_agent
from langchain.agents import AgentType
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredURLLoader

import requests

import yfinance as yf
import json

# --- Environment variables --- #
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
serpkey = os.getenv("SERPAPI_API_KEY")
apilayerkey = os.getenv("API_LAYER_API_KEY")

# --- Output format for stock outputs --- #
json_schema = {
    "title": "Company",
    "description": "Information about the company",
    "type": "object",
    "properties": {
        "name": {"title": "Name", "description": "The company's name", "type": "string"},
        "news": {"title": "News", "description": "The recent news about the company", "type": "string"},
        "stockPrice": {"title": "Price", "description": "The company's stock price"},
        "recommend": {"title": "Recommend", "description": "If it is recommended to buy this stock"}
    }
}

# --- Output format for news outputs --- #
json_news_schema = {
    "title": "Company",
    "description": "Information about the company",
    "type": "object",
    "properties": {
        "name": {"title": "Name", "description": "The company's name", "type": "string"},
        "news": {"title": "News", "description": "The recent news about the company", "type": "string"},
        "url": {"title": "Url", "description": "The url from the source"},
    }
}

# --- Setting up language model --- #
llm = ChatOpenAI(model="gpt-4", openai_api_key=key)

# --- Loads serpapi tool, sets the language model to use, and sets the api key --- #
tools = load_tools(["serpapi"], llm=llm, serpapi_api_key=serpkey)

search = SerpAPIWrapper()

# --- Define a list of tools offered by the agent --- #
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful when you need to answer questions about current events. You should ask targeted questions.",
    ),
]

mrkl = initialize_agent(
    tools, llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
)

# --- Prompt for extracting news sources --- #
prompt_msgs = [
    SystemMessage(
        content="You are a world class algorithm for extracting new information about large companies."
    ),
    HumanMessage(
        content="Extract the name of the company, news title, and the source url from the following input:"
    ),
    HumanMessagePromptTemplate.from_template("{input}"),
    HumanMessage(content="Tips: Make sure to answer in the correct format"),
]

# --- Prompt for extraction yahoo finance information --- #
messages = [
    SystemMessage(
        content="You are a world class algorithm for extraction information from JSON format."
    ),
    HumanMessage(
        content="Extract the company name, stock prices, and if it is recommended to buy from the following input:"
    ),
    HumanMessagePromptTemplate.from_template("{input}"),
    HumanMessage(
        content="Tips: Make sure to answer in the correct format."
    )
]

# --- Retrieves news --- #
def retrieveNews(input):
    prompt = ChatPromptTemplate(messages=prompt_msgs)
    url = f"https://api.apilayer.com/financelayer/news?tickers={input}"

    payload = {}
    headers= {
        "apikey": apilayerkey
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    result = response.text

    chain = create_structured_output_chain(json_news_schema, llm, prompt, verbose=True)
    return chain.run(json.dumps(result))

# --- Retrieves Stock Prices --- #
def retrieveStocks(company_name: str):
    prompt = ChatPromptTemplate(messages=messages)
    comp = yf.Ticker(company_name)

    chain = create_structured_output_chain(json_schema, llm, prompt, verbose=True)
    return chain.run(json.dumps(comp.info))

# --- Identifies ticker in text --- #
def retrieveTicker(input):
    msgs = [
        SystemMessage(
            content="You are a helpful assistant who retrieves the company ticker from a string of text."
        ),
        HumanMessage(
            content="Extract the company ticker from the following input:"
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        HumanMessage(content="Tips: Make sure to answer in the correct format")
    ]

    prompt = ChatPromptTemplate(messages=msgs)
    json_schema = {
        "title": "Company",
        "description": "Company Ticker",
        "type": "object",
        "properties": {
            "ticker": {"title": "ticker", "description": "The company's ticker", "type": "string"},
        }
    }

    chain = create_structured_output_chain(json_schema, llm, prompt, verbose=True)
    return chain.run(input)

# --- Decision prompt; helps LLM decide which function to call --- #
msgs = [
    SystemMessage(
        content="You are a helpful assistant who retrieves the latest information about a large company."
    ),
    HumanMessage(
        content="Make calls to the relevant function to record information in the following input:"
    ),
    HumanMessagePromptTemplate.from_template("{input}"),
    HumanMessage(content="Tips: Make sure to answer in the correct format")
]

# --- Generates Response --- #
def generate(text):
    prompt = ChatPromptTemplate(messages=msgs)

    input = text

    chain = create_openai_fn_chain([retrieveNews, retrieveStocks], llm, prompt, verbose=True)
    decision = chain.run(input)
    print(decision)


    if (decision["name"] == "retrieveNews"):
        ticker = retrieveTicker(input)
        #Sets output as variable
        newsReply = retrieveNews(ticker["ticker"])
        
        return newsReply

    elif decision["name"] == "retrieveStocks":
        #Sets output as variable
        tickerReply = retrieveStocks(decision["arguments"]["company_name"])
        return llm.predict(f"Can you summarize this?: {tickerReply}")
