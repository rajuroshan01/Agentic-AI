def general_agent(state: AgentState):
    state["response"] = llm.predict(state["user_input"])
    return state