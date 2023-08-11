# --- Imports --- #
import os
from dotenv import load_dotenv

from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.utilities import SerpAPIWrapper
from langchain import SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, load_tools, AgentType
from langchain.chat_models import ChatOpenAI
import yfinance as yf
import json

from QA.qa import urlSummarizer

# --- Environment variables --- #
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
serpkey = os.getenv("SERPAPI_API_KEY")
apilayerkey = os.getenv("API_LAYER_API_KEY")
newsapikey = os.getenv("NEWSAPI_API_KEY")


def retrieveNews(company_name: str) -> str:
    pass


def retrieveStocks(company_name: str) -> str:
    pass


def questionsAboutCurrent(input: str) -> str:
    pass


def generalConversation(input: str) -> str:
    pass


"""
TO-DO:
1. Broaden search query
2. Allow external URL summarization
3. Fix all bugs with search
4. Fix object oriented approach
"""


class Blijax:
    def __init__(self, ai_model: str, summarize_length: str):
        self.ai_model = ai_model
        self.summarize_length = summarize_length
        self.llm = ChatOpenAI(model=ai_model, openai_api_key=key)
        self.search = SerpAPIWrapper()
        self.tools = load_tools(["serpapi"], llm=self.llm, serpapi_api_key=serpkey)
        self.tools = [
            Tool(
                name="Search",
                func=self.search.run,
                description="Useful when you need to answer questions about current events. You should ask targeted questions.",
            ),
        ]
        self.agent = initialize_agent(
            self.tools, self.llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True
        )

        self.json_schema = {
            "title": "Company",
            "description": "Information about the company",
            "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "description": "The company's name",
                    "type": "string",
                },
                "news": {
                    "title": "News",
                    "description": "The recent news about the company",
                    "type": "string",
                },
                "stockPrice": {
                    "title": "Price",
                    "description": "The company's stock price",
                },
                "recommend": {
                    "title": "Recommend",
                    "description": "If it is recommended to buy this stock",
                },
            },
        }

        # --- Output format for news outputs --- #
        self.json_news_schema = {
            "title": "Company",
            "description": "Information about the company",
            "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "description": "The company's name",
                    "type": "string",
                },
                "news": {
                    "title": "News",
                    "description": "The recent news about the company",
                    "type": "string",
                },
                "url": {"title": "Url", "description": "The url from the source"},
            },
        }

        self.json_conversation_schema = {
            "properties": {
                "text": {
                    "title": "text",
                    "description": "the text response",
                    "type": "string",
                },
            }
        }

        self.news_messages = [
            SystemMessage(
                content="You are a world class algorithm for extracting new information about large companies."
            ),
            HumanMessage(
                content="Extract the name of the company, news title, and the source url from the following input:"
            ),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(
                content="Tips: Make sure to answer in the correct format and choose the most relevant source based on the title."
            ),
        ]

        # --- Prompt for extraction yahoo finance information --- #
        self.stock_messages = [
            SystemMessage(
                content="You are a world class algorithm for extraction information from JSON format."
            ),
            HumanMessage(
                content="Extract the company name, stock prices, and if it is recommended to buy from the following input:"
            ),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(content="Tips: Make sure to answer in the correct format."),
        ]

        self.personal_context = [
            SystemMessage(
                content="You are Blijax, an assistant who helps answer questions. If you don't know something, say you don't know."
            ),
            HumanMessage(content="Repond accordingly to this input:"),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(content="Tips: Make sure to answer in the correct format."),
        ]

        self.stock_prompt = ChatPromptTemplate(messages=self.stock_messages)
        self.news_prompt = ChatPromptTemplate(messages=self.news_messages)

        self.stock_chain = create_structured_output_chain(
            self.json_schema, self.llm, self.stock_prompt, verbose=True
        )
        self.news_chain = create_structured_output_chain(
            self.json_news_schema, self.llm, self.news_prompt, verbose=True
        )

        # self.decision_chain = None

    # --- Define a list of tools offered by the agent --- #
    def setUpChain(self, functions_list):
        msgs = [
            SystemMessage(
                content="You are a helpful assistant who retrieves the latest information about large companies."
            ),
            HumanMessage(
                content="Make calls to the relevant function to record information in the following input:"
            ),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(content="Tips: Make sure to answer in the correct format."),
        ]
        prompt = ChatPromptTemplate(messages=msgs)

        self.decision_chain = create_openai_fn_chain(
            functions_list, self.llm, prompt, verbose=True
        )

    # --- Prompt for extracting news sources --- #

    # --- Retrieves news --- #
    def retrieveNews(self, company_name: str) -> str:
        import requests

        url = (
            "https://newsapi.org/v2/everything?"
            f"q={company_name}&"
            "from=2023-08-08&"
            "sortBy=popularity&"
            f"apiKey={newsapikey}"
        )

        response = requests.request("GET", url)

        result = response.text
        result = json.loads(result)
        # jsonResponse = self.news_chain.run(json.dumps(result))

        articles = [result["articles"][0]]
        urls = [i["url"] for i in articles]
        print(urls)
        returned = []
        for i in urls:
            returned.append(urlSummarizer(i))
            print("url_summarized")
        print(returned)
        return returned

    # --- Retrieves Stock Prices --- #
    def retrieveStocks(self, company_name: str, questionAboutStock: str) -> str:
        self.stock_messages = [
            SystemMessage(
                content="You are a world class algorithm for extraction information from JSON format."
            ),
            HumanMessage(
                content=f"Given this input, answer this question: {questionAboutStock}"
            ),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(content="Tips: Make sure to answer in the correct format."),
        ]
        self.stock_prompt = ChatPromptTemplate(messages=self.stock_messages)
        self.stock_chain.prompt = self.stock_prompt

        comp = yf.Ticker(company_name)
        return self.stock_chain.run(json.dumps(comp.info))

    # --- Identifies ticker in text --- #
    def retrieveTicker(self, input):
        msgs = [
            SystemMessage(
                content="You are a helpful assistant who retrieves the company ticker from a string of text."
            ),
            HumanMessage(
                content="Extract the company ticker from the following input:"
            ),
            HumanMessagePromptTemplate.from_template("{input}"),
            HumanMessage(content="Tips: Make sure to answer in the correct format"),
        ]

        prompt = ChatPromptTemplate(messages=msgs)
        json_schema = {
            "title": "Company",
            "description": "Company Ticker",
            "type": "object",
            "properties": {
                "ticker": {
                    "title": "ticker",
                    "description": "The company's ticker",
                    "type": "string",
                },
            },
        }

        chain = create_structured_output_chain(
            json_schema, self.llm, prompt, verbose=True
        )
        return chain.run(input)

    def questionsAboutCurrent(self, input) -> str:
        """
        Good for checking questions about current events, weather updates, or things similar.
        """
        return self.agent.run(input)

    def generalConversation(self, input) -> str:
        return self.llm.predict(
            f"""You are Blijax, an assistant who helps answer questions. Respond accordingly to this input: {input} 
            Sometimes use emojis to express your emotions."""
        )

    # --- Decision prompt; helps LLM decide which function to call --- #
    msgs = [
        SystemMessage(
            content="You are a helpful assistant who retrieves the latest information about large companies."
        ),
        HumanMessage(
            content="Make calls to the relevant function to record information in the following input:"
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        HumanMessage(
            content="Tips: Make sure to answer in the correct format, and calling the questionsAboutCurrent function will give you the power to search the internet."
        ),
    ]

    # --- Generates Response --- #
    def generate(self, text):
        # prompt = ChatPromptTemplate(messages=self.msgs)

        input = text
        # [self.retrieveNews, self.retrieveStocks, self.questionsAboutCurrent, self.generalConversation]
        # [retrieveNews, retrieveStocks, questionsAboutCurrent, generalConversation]

        if not self.decision_chain:
            pass

        decision = self.decision_chain.run(input)
        print(decision)

        if decision["name"] == "retrieveNews":
            # ticker = self.retrieveTicker(input)

            newsReply = self.retrieveNews(decision["arguments"]["company_name"])
            newsReply = "".join(newsReply)

            return newsReply

        elif decision["name"] == "retrieveStocks":
            ticker = self.retrieveTicker(input)
            print(ticker["ticker"])
            tickerReply = self.retrieveStocks(ticker["ticker"], input)
            return self.llm.predict(f"Can you summarize this?: {tickerReply}")

        elif decision["name"] == "questionsAboutCurrent":
            return self.questionsAboutCurrent(input)

        elif decision["name"] == "generalConversation":
            return self.generalConversation(input)
