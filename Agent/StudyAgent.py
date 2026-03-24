def study_agent(state: AgentState):
    prompt = f"""
    You are a teacher.

    Explain clearly:
    {state['user_input']}
    """

    state["response"] = llm.predict(prompt)
    return state