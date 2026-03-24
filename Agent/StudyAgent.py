from LLM.llm import llm
from langchain_core.messages import HumanMessage, AIMessage
def study_agent(state):
    prompt = f"""
    Memory = {state["messages"]}
    You are a teacher.

    Explain clearly:
    {state['user_input']}
    """

    res = llm.invoke(prompt).content
    state["response"] = res
    state["messages"].append(AIMessage(content=res))
    return state