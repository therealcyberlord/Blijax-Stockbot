#Imports
import os
import sys
import codecs
import requests
import nltk
import string
import random

#langchain
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import SeleniumURLLoader
from bs4 import BeautifulSoup

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

#import dotenv
from dotenv import load_dotenv

#loading dotenv
load_dotenv()

#openai API key from .env
key = os.getenv("OPENAI_API_KEY")


#Extracts URL
def extract_text_from(url):
     html = requests.get(url).text
     soup = BeautifulSoup(html, features="html.parser")
     text = soup.get_text()

     lines = (line.strip() for line in text.splitlines())
     return '\n'.join(line for line in lines if line)

#Sets text to all info
text = extract_text_from("https://en.wikipedia.org/wiki/Quantum_mechanics")

#def urlSummarizer(text): 
 # initializing size of string

def urlSummarizer(text):
  urls = ["https://en.wikipedia.org/wiki/Quantum_mechanics"]

  loader = SeleniumURLLoader(urls=urls)

  index = VectorstoreIndexCreator().from_loaders([loader])

  #printing the answer
  return index.query("Paraphrase this into a couple key points in a minium of five sentence")

