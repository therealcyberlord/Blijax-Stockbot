# --- Imports --- #
import os
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import SeleniumURLLoader
from dotenv import load_dotenv

#loading dotenv
load_dotenv()

#openai API key from .env
key = os.getenv("OPENAI_API_KEY")

# --- Loads url data, splits it into chunks --- #
def urlSummarizer(url: str, summarize_length: str):
  urls = [url]

  loader = SeleniumURLLoader(urls=urls)

  index = VectorstoreIndexCreator().from_loaders([loader])
  """
  VectorstoreIndexCreator:
  It takes in document loaders and loads the documents from them.
  It splits the loaded documents into chunks using a text splitter (by default CharacterTextSplitter). The text splitter splits each document into smaller chunks.
  It generates embeddings for each chunk using a specified embedding method (by default OpenAIEmbeddings).
  It stores the chunks and their corresponding embeddings in a vectorstore (by default Chroma). The vectorstore acts as a search index.
  It exposes the vectorstore in a retriever interface, so the vectorstore can be used to retrieve relevant documents for a query.
  It wraps all this functionality in a simple API - VectorstoreIndexCreator.from_loaders() - which takes in document loaders and handles splitting, embedding and indexing the documents automatically.
  """
  return index.query(f"Paraphrase this into a couple key points in {summarize_length}")

