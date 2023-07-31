import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()

key = os.getenv("API_KEY")

llm = OpenAI(openai_api_key=key)

text = input("Enter a question...")

print(llm.predict(text))
