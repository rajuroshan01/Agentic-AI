from LLM.llm import llm
from langchain_core.messages import HumanMessage, AIMessage
def travel_agent(state):
    prompt = f"""
    Memory = {state["messages"]}
    You are a travel planner. Analyse the Memory and respond the travel related query.

    Question is last element of the Memory array.
    """
    res = llm.invoke(prompt).content

    print("Prompttttt>>>>>>>>>>>>",prompt)
    print(f"response...................{res}")
    state["response"] = res
    state["messages"].append(AIMessage(content=res))
    return state