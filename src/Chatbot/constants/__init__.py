EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
PINECONE_INDEXNAME = "stockbot"

# CUSTOM_PROMPT_TEMPLATE = """
# Use the pieces of information provided in the context to answer the users questions.
# If you don't know the answer, just say that you don't know, don't try to make up an answer.
# Please start to answer directly, no small talks and don't start the answer with 'Answer:'.

# Context: {context}
# Question: {question}
# """

CUSTOM_PROMPT_TEMPLATE = """
Use the provided context to answer the user's question. Do not start with "Answer:" or any such prefix in the response. 
If the answer is unknown, state that you don't know without making up information.
Don't provide provide anything out of the given context

Context: {context} 
Question: {question} 

Start the answer directly, no small talks please.
"""

HUGGING_FACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
