from src.core import llm
from src.app.schemas import State
from langchain_core.messages import HumanMessage, SystemMessage

def tech_lead(state: State):
    
    messages = [SystemMessage("You are a highly experience Lech lead of a team of developers You are given a short description of a project and your task is to provide a detailed technical plan for the project."), HumanMessage(state["requirements"])]
    state["tech_lead"] = llm.invoke(messages).content
    return state