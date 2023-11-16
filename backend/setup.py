import os
from dotenv import load_dotenv
load_dotenv()
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from openai_token import OPENAI_TOKEN

os.environ["OPENAI_API_KEY"] = OPENAI_TOKEN
os.makedirs('./index',exist_ok=True)

documents = SimpleDirectoryReader('./index').load_data()

index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist('./index')