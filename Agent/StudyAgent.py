from LLM.llm import llm
from Tools.toolsetup import llm_with_tools
from langchain_core.messages import HumanMessage, AIMessage

def study_agent(state):
    prompt = f"""
    Memory = {state["messages"]}
    You are a teacher. call the tool `get_status`, if status is True then

    Explain clearly:
    {state['user_input']}

    If status is False then Just say " I can't help you with this".
    """
    print("prompt",prompt)
    res = llm_with_tools.invoke(prompt).content
    print("Test_tool", res)
    state["response"] = res
    state["messages"].append(AIMessage(content=res))
    return state