from langgraph.graph import StateGraph
from typing import TypedDict
from Agent.GeneralAgent import general_agent
from Agent.StudyAgent import study_agent
from Agent.TravelAgent import travel_agent

class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str

# Orchestrator
def orchestrator(state):
    text = state["user_input"].lower()

    if "trip" in text:
        state["intent"] = "travel"
    elif "aws" in text:
        state["intent"] = "study"
    else:
        state["intent"] = "general"

    return state

# Agents
def travel_agent(state):
    state["response"] = "Here is your travel plan ✈️"
    return state

def study_agent(state):
    state["response"] = "AWS is a cloud platform ☁️"
    return state

def general_agent(state):
    state["response"] = "How can I help you?"
    return state

# Router
def router(state):
    return state["intent"]

# Build graph
builder = StateGraph(AgentState)

builder.add_node("orchestrator", orchestrator)
builder.add_node("travel", travel_agent)
builder.add_node("study", study_agent)
builder.add_node("general", general_agent)

builder.set_entry_point("orchestrator")

builder.add_conditional_edges(
    "orchestrator",
    router,
    {
        "travel": "travel",
        "study": "study",
        "general": "general"
    }
)

graph = builder.compile()

