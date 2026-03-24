from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.4,
    api_key=os.getenv("OPENAI_KEY")
)

#response = llm.invoke("Tell me about yourself.")