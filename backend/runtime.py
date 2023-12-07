import streamlit as st
import json
import os
from dotenv import load_dotenv
load_dotenv()
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from chat_helper import ChatHelper
from openai_token import OPENAI_TOKEN

os.environ["OPENAI_API_KEY"] = OPENAI_TOKEN

# rebuild storage context
# storage_context = StorageContext.from_defaults(persist_dir='./data')
loader = SimpleDirectoryReader('./data', required_exts='*.txt')
documents = loader.load_data()
# load index
index = GPTVectorStoreIndex.from_documents(documents)

# Create the chatbot

if __name__ == "__main__":

    st.title("Chatbot")

    # User ID
    user_id = st.text_input("Your Name:")
    # Check if user ID is provided
    if user_id:
        # Create chatbot instance for the user
        bot = ChatHelper(OPENAI_TOKEN, index, user_id)

        # Load chat history
        bot.load_chat_history()

        # Display chat history
        for message in bot.chat_history[-6:]:
            st.write(f"{message['role']}: {message['content']}")

        # User input
        user_input = st.text_input("Type your questions here :) - ")

        # Generate response
        if user_input:
            bot_response = bot.generate_response(user_input)
            bot_response_content = bot_response['content']
            st.write(f"{user_id}: {user_input}")
            st.write(f"Bot: {bot_response_content}")
            bot.save_chat_history()
            bot.chat_history.append({"role": "user", "content": user_input})
            bot.chat_history.append({"role": "assistant", "content": bot_response_content})