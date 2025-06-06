from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

from agents.weather_agent import weather_agent
from agents.stock_agent import stock_agent
from agents.news_agent import news_agent
from agents.router_agent import router_agent
from agents.general_agent import general_agent

# Define the state schema
class GraphState(TypedDict):
    input: str
    result: str

# Helper to update state
def get_state_update(output: str) -> dict:
    return {"result": output}

# Map routes to agents
agent_map = {
    "weather": weather_agent,
    "stock": stock_agent,
    "news": news_agent,
    "general": general_agent,

}

# Node logic: router + call agent
def route_and_call(state: dict):
    user_input = state["input"]
    route = router_agent.invoke(user_input)
    agent = agent_map.get(route)
    if agent:
        output = agent.invoke(user_input)
        return get_state_update(output)
    return get_state_update("Sorry, I didn't understand that.")

# Build graph
builder = StateGraph(GraphState)
builder.add_node("router", RunnableLambda(route_and_call))
builder.set_entry_point("router")
builder.set_finish_point("router")

graph = builder.compile()
