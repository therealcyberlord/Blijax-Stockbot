import os
import sys
import codecs
from newspaper import Article
import nltk
#import dotenv
from dotenv import load_dotenv

#langchain
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders import SeleniumURLLoader

#loading dotenv
load_dotenv()

key = os.getenv("OPENAI_API_KEY")

#openai API key from .env


#query set to terminal answer
# to run type this in terminal:  python3 Blijax-Stockbot/blijax_backend/QA/qa.py "Sum up the information into a couple sentences getting the key points"  
# at the end of the command there is a section of text with apostrophes. That section is the prompt. Feel free to mess around with the prompt. 
#query = sys.argv[1]


#loading the TXT data into loader

#for single txt files
#loader = TextLoader('Blijax-Stockbot/blijax_backend/QA/qaTEXT.txt')

#For multiple url's
#loader = read("https://www.fitchratings.com/research/sovereigns/fitch-downgrades-united-states-long-term-ratings-to-aa-from-aaa-outlook-stable-01-08-2023")

url = 'https://www.fitchratings.com/research/sovereigns/fitch-downgrades-united-states-long-term-ratings-to-aa-from-aaa-outlook-stable-01-08-2023'
article = Article(url)

articleINFO = article.text

#loader = TextLoader(article.text)

with open('Blijax-Stockbot/blijax_backend/generate/language.txt', 'w') as f:
  f.write(repr(articleINFO) + '\n')     


#Storing the vector index with the data through the loader
#index = VectorstoreIndexCreator().from_loaders([loader])

#printing the answer
#print(index.query("Paraphrase this into a couple key points in a couple sentences"))



# || Below is info for implementing into other code or frontend ||

# do
# import qa.py
# and to set variables do qa.variableName 
# example: qa.loader = TextLoader('qaTEXT.txt') || This sets the loader with the data to be used

#when using this you can change it to implement to other things by setting the fully nested query in print on line 29 to "Sum up the information into a couple sentences getting the key points"
#Then you should be able to set the loader variable, index variable, and then run line 29 to get the output

# once this is done you can add a way to change/add to the qaTEXT by doing a with open function on the txt file from where you are calling/using qa.py 
# after that is done you should be able to access the txt file and run the code to recieve an output