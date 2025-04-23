from Chatbot.components.document_processor import load_documents, create_chunks
from Chatbot.components.model import get_embedding_model
from Chatbot.components.pinecone_embedding import create_vector_db, store_embedding
from dotenv import load_dotenv
from pathlib import Path
from Chatbot.constants import EMBEDDING_MODEL, PINECONE_INDEXNAME
import os

load_dotenv()
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

def processing():
  documents = load_documents(Path("C:\\Users\\tusha_00pr59a\\OneDrive\\Desktop\\project\\ChatBot\\Data\\"))
  data_chunks = create_chunks(documents)

  embedding_model = get_embedding_model(EMBEDDING_MODEL)

  create_vector_db(PINECONE_API_KEY, PINECONE_INDEXNAME)

  store_embedding(data_chunks, embedding_model, PINECONE_INDEXNAME)

processing()