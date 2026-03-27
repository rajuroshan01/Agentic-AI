from langgraph.graph import StateGraph
from typing import TypedDict
from Agent.GeneralAgent import general_agent
from Agent.StudyAgent import study_agent
from Agent.TravelAgent import travel_agent
from LLM.llm import llm
from ContextMemory.context import memory
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import ToolNode
from Tools.toolsetup import tools

tool_node = ToolNode(tools)
class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str
    messages : list

# Orchestrator
def orchestrator(state):
    if "messages" not in state:
        state["messages"] = []
    state["messages"].append(HumanMessage(content=state["user_input"]))
    
    prompt = f"""
    Classify the user query into one of these:
    - travel
    - study
    - general

    User Query: {state["user_input"]}

    Return only one word.

    """
    response = llm.invoke(prompt)
    state["intent"] = response.content.strip().lower()
    return state

# Agents
def travelagent(state):
    state = travel_agent(state)
    return state

def studyagent(state):
    state = study_agent(state)
    return state

def generalagent(state):
    state = general_agent(state)
    return state

# Router
def router(state):
    return state["intent"]

# Build graph
builder = StateGraph(AgentState)

builder.add_node("orchestrator", orchestrator)
builder.add_node("travel", travelagent)
builder.add_node("study", studyagent)
builder.add_node("tools",tool_node)

builder.add_node("general", generalagent)
builder.add_edge("tools", "study")

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

graph = builder.compile(checkpointer=memory)

