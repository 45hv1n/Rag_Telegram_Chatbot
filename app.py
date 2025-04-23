from chain import get_qa_chain
from Chatbot.components.model import load_mistral_model, get_embedding_model
from Chatbot.components.pinecone_embedding import get_vector_data
from Chatbot.constants import CUSTOM_PROMPT_TEMPLATE, PINECONE_INDEXNAME, EMBEDDING_MODEL, HUGGING_FACE_REPO_ID
import os 
from dotenv import load_dotenv
import asyncio

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

load_dotenv()

HF_TOKEN = os.environ["HF_TOKEN"]
os.environ["HF_TOKEN"] = HF_TOKEN

PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

mistral_model = load_mistral_model(HF_TOKEN, HUGGING_FACE_REPO_ID)
embedding_model = get_embedding_model(EMBEDDING_MODEL)


qaChain = get_qa_chain(mistral_model,
                       get_vector_data(embedding_model, PINECONE_INDEXNAME),
                       CUSTOM_PROMPT_TEMPLATE)

def invokeChain(user_query):
    response = qaChain.invoke({"query": user_query})
    return response["result"]

### Create a bot 

async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id= update.effective_chat.id, action= ChatAction.TYPING)
    await asyncio.sleep(5)
    await update.message.reply_text("Welcome to Arth Kosh! 📈 Your personal finance and stock market assistant. Ask questions about finance, stocks, investments, or anything from our curated collection of financial books. Type /help to see available commands or simply ask a question to get started!")

async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id= update.effective_chat.id, action= ChatAction.TYPING)
    await asyncio.sleep(5)
    await update.message.reply_text(""" 
        Arth Kosh is here to answer your finance and stock market queries! 📚 Here's how to use me: Ask a Question: Type your question (e.g., "What is a P/E ratio?" or "How to diversify a portfolio?").
        Commands:
            /start: Begin or restart the bot.
            /help: Show this guide.
        """)

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id= update.effective_chat.id, action= ChatAction.TYPING)
    msg_type = update.message.chat.type
    text = update.message.text

    if msg_type == "group":
        return
    else:
        await context.bot.send_chat_action(chat_id= update.effective_chat.id, action= ChatAction.TYPING)
        await asyncio.sleep(5)
        response = invokeChain(text)
        print("Bot response: ", response)

    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Bot error: ", context.error)


if __name__ == '__main__':
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", startCommand))
    app.add_handler(CommandHandler("help", helpCommand))
    app.add_handler(MessageHandler(filters.TEXT, handle_msg))

    app.add_error_handler(error)

    print("Polling")
    
    app.run_polling(poll_interval = 3,)

# user_query = "What is stocks"

# response = qaChain.invoke({"query": user_query})

# print(" Response :", response["result"])