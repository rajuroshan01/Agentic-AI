from langchain.tools import tool
from LLM.llm import llm

@tool
def get_status():
    """This is status of LLM response"""
    print("get_status tool")
    return True


tools = [get_status]

llm_with_tools = llm.bind_tools(tools)

    



