from langgraph.graph import StateGraph
from typing import TypedDict

class State(TypedDict):
    requirements: str
    tech_lead: str