from langgraph.graph import StateGraph
from src.app.nodes.tech_lead import tech_lead
from src.app.schemas import State

builder = StateGraph(State)

builder.add_node("tech_lead", tech_lead)
builder.set_entry_point("tech_lead")

graph = builder.compile()

result = graph.invoke(
    {"requirements": "Hi, can you make a calculator app"}
)

print(result)
