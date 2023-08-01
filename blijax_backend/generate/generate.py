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

from typing import Optional

from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from pydantic import BaseModel, Field

from langchain.memory import ChatMessageHistory

from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.utilities import SerpAPIWrapper

from langchain.agents import load_tools

import requests

from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, create_pandas_dataframe_agent
from langchain.agents import AgentType

import yfinance as yf
import json

# --- Environment variables --- #
load_dotenv()

key = os.getenv("API_KEY")
serpkey = os.getenv("SERPAPI_API_KEY")

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

prompt_msgs = [
    SystemMessage(
        content="You are a world class algorithm for extracting new information about large companies."
    ),
    HumanMessage(
        content="Use the given format to extract information from the following input:"
    ),
    HumanMessagePromptTemplate.from_template("{input}"),
    HumanMessage(content="Tips: Make sure to answer in the correct format"),
]

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

def retrieveNews(input):
    prompt = ChatPromptTemplate(messages=prompt_msgs)

    chain = create_structured_output_chain(json_schema, llm, prompt, verbose=True)
    return chain.run(mrkl.run(input))


def retrieveStocks(company_name: str):
    prompt = ChatPromptTemplate(messages=messages)
    comp = yf.Ticker(company_name)

    chain = create_structured_output_chain(json_schema, llm, prompt, verbose=True)
    return chain.run(json.dumps(comp.info))

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

prompt = ChatPromptTemplate(messages=msgs)

input = "What is the latest news on tesla?"

chain = create_openai_fn_chain([retrieveNews, retrieveStocks], llm, prompt, verbose=True)
decision = chain.run(input)
print(decision)

if (decision["name"] == "retrieveNews"):
    print(retrieveNews(input))
elif decision["name"] == "retrieveStocks":
    print(retrieveStocks(decision["arguments"]["company_name"]))
