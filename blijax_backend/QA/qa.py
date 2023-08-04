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
from newspaper import Article
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



def urlSummarizer(text): 
 # initializing size of string
 N = 10
 
 # using random.choices()
 # generating random strings
 res = ''.join(random.choices(string.ascii_uppercase +
                              string.digits, k=N))

 f = open(res + ".txt", "x")

 with open(res + '.txt', 'w') as f:
   f.write(repr(text) + '\n')     



 #Sets file to loader
 loader = TextLoader(res + ".txt")

 #Storing the vector index with the data through the loader
 index = VectorstoreIndexCreator().from_loaders([loader])

 #printing the answer
 print(index.query("Paraphrase this into a couple key points in a minium of five sentence"))

 #removes the file
 os.remove(res + ".txt")