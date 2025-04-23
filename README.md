### RAG Chatbot with Pinecone, Mistral, and Telegram

This project is a Retrieval-Augmented Generation (RAG) chatbot that leverages a vector database (Pinecone), the Mistral language model, and a Telegram bot interface. The chatbot uses semantic search to retrieve relevant context from embedded book data stored in Pinecone, which is then used by the Mistral model to generate accurate and contextually relevant responses. The bot is accessible via Telegram, allowing users to interact seamlessly.

#### Features

- Semantic Search: Uses embeddings stored in Pinecone to perform semantic search for retrieving relevant book content based on user queries.
- RAG Pipeline: Combines retrieved context with the Mistral model to generate high-quality responses.
- Telegram Integration: Users can interact with the chatbot through a Telegram bot.
- Scalable Vector DB: Pinecone is used for efficient storage and retrieval of text embeddings.
- Modular Design: Easy-to-understand scripts for data processing and bot operation.

#### Tech Stack

- Python: Core programming language.
- Pinecone: Vector database for storing and querying embeddings.
- LangChain: Framework for building the RAG pipeline and managing embeddings.
- Mistral Model: Language model for generating responses.
- HuggingFace: Provides access to embeddings and model APIs.
- Telegram Bot: Interface for user interaction via Telegram.

#### Prerequisites

Before running the project, ensure you have the following:
- Pinecone account and API key (sign up at Pinecone).
- HuggingFace account and API token (sign up at HuggingFace).
- Telegram bot and its token (create one via BotFather on Telegram).

#### Installation

Follow these steps to set up and run the project:

##### Clone the Repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

##### Install the required Python packages by running:

pip install -r requirements.txt

##### Set Up Environment Variables:

Create a .env file in the project root and add the following keys:
- PINECONE_API_KEY=your_pinecone_api_key
- HUGGINGFACE_TOKEN=your_huggingface_token
- TELEGRAM_TOKEN=your_telegram_bot_token

Replace your_pinecone_api_key, your_huggingface_token, and your_telegram_bot_token with your actual credentials.

- Process Data and Create Vector DB: Run the data_processing.py script to generate embeddings from the book data and store them in Pinecone:
python data_processing.py

This script processes the books, creates embeddings, and uploads them to the Pinecone vector database.

- Run the Chatbot: Start the Telegram bot and the RAG pipeline by running:
python app.py

This script initializes the QA chain (using LangChain and Mistral) and starts polling the Telegram bot for user queries.

##### Usage

Open Telegram and start a chat with your bot (use the bot name provided by BotFather).
Send a query related to the book content.
The bot performs a semantic search in Pinecone, retrieves relevant context, and generates a response using the Mistral model.
The response is sent back to you in the Telegram chat.

##### Project Structure

data_processing.py: Script to process book data, generate embeddings, and store them in Pinecone.
app.py: Main script to run the RAG pipeline and Telegram bot.
requirements.txt: List of Python dependencies.
.env: Environment file for storing API keys and tokens (not tracked in git).
Data/: Directory containing the book data (not included in the repo; add your own books).

License
This project is licensed under the MIT License. See the LICENSE file for details.
