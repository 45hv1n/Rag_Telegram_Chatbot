from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec

### Creating a vector DB in Pinecone

def create_vector_db(api_key, index_name):
    pc = Pinecone(api_key = api_key)

    print("@@@@@@#@@ create vector  db ", pc.list_indexes().names())

    if index_name in pc.list_indexes().names():
        pc.delete_index(index_name)

    pc.create_index(
        name= index_name,
        dimension= 384,
        metric= "cosine",
        spec= ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

def store_embedding(data_chunks, vector_embedding_model, vectorDB_index_name):
    print("@@@@@@#@@ create vector  data ")
    vectorStore = PineconeVectorStore.from_documents(data_chunks, vector_embedding_model, index_name = vectorDB_index_name)

def get_vector_data(vector_embedding_model, index_name):
   print("@@@@@@#@@ get vector data ")
   vectorData = PineconeVectorStore.from_existing_index(
                    embedding = vector_embedding_model,
                    index_name = index_name)
   return vectorData