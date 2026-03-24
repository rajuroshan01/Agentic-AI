from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0,
    openai_api_key=""
)

