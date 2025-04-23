from langchain_huggingface import HuggingFaceEndpoint
from langchain.embeddings import HuggingFaceEmbeddings

### The model consist of 384 dense dimension.
def get_embedding_model(embedding_model):
    print("@@@@@@#@@ loading embedding model ")
    vector_embedding_model = HuggingFaceEmbeddings(model_name = embedding_model)
    print("@@@@@@#@@ loadied embedding model ")
    return vector_embedding_model


def load_mistral_model(token, repo_id):

    print("@@@@@@#@@ loading mistral model ")
    model = HuggingFaceEndpoint(
        repo_id = repo_id,
        temperature = 0.5,
        task="text-generation",
        max_new_tokens =  512,
        model_kwargs = {
            "max_length": 512,
            "token": token
        }
    )
    return model

get_embedding_model("sentence-transformers/all-MiniLM-L6-v2")