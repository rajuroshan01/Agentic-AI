from LLM.llm import llm
from langchain_core.messages import HumanMessage, AIMessage
def general_agent(state):
    res = llm.invoke(state["user_input"]).content
    state["response"] = res
    state["messages"].append(AIMessage(content=res))
    return state