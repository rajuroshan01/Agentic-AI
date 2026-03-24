def travel_agent(state: AgentState):
    prompt = f"""
    You are a travel planner.

    User: {state['user_input']}
    Give a helpful travel plan.
    """

    state["response"] = llm.predict(prompt)
    return state