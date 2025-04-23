from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

### Loads the documents using the path of the data
def load_documents(data_path: Path):
  print("@@@@@@#@@ loading  data ")
  documents_loader = DirectoryLoader(data_path, glob = "*.pdf", loader_cls= PyPDFLoader)
  doc = documents_loader.load()
  return doc

### Creates chunks of the extracted data
def create_chunks(extracted_data):
  print("@@@@@@#@@ chunking  data ")
  text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
  chunks = text_splitter.split_documents(extracted_data)
  return chunks