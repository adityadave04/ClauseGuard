from typing import TypedDict

from langgraph.graph import StateGraph, END

from agent.tools import AskTool
from agent.risk_scanner import RiskScanner
from agent.extractor import MetadataExtractor



class AgentState(TypedDict):

    query: str
    response: dict | str


ask_tool = AskTool()
risk_tool = RiskScanner()
extract_tool = MetadataExtractor()

ask_tool = AskTool()
risk_tool = RiskScanner()
extract_tool = MetadataExtractor()

def ask_node(state):

    result = ask_tool.ask(
        state["query"]
    )

    return {
        "response": result
    }


def risk_node(state):

    result = risk_tool.scan()

    return {
        "response": result
    }


def extract_node(state):

    result = extract_tool.extract()

    return {
        "response": result
    }


def router(state):

    query = state["query"].lower()

    if "risk" in query:
        return "risk"

    if "extract" in query:
        return "extract"

    return "ask"

graph = StateGraph(AgentState)

graph.add_node("ask", ask_node)
graph.add_node("risk", risk_node)
graph.add_node("extract", extract_node)

graph.set_conditional_entry_point(
    router,
    {
        "ask": "ask",
        "risk": "risk",
        "extract": "extract"
    }
)

graph.add_edge("ask", END)
graph.add_edge("risk", END)
graph.add_edge("extract", END)

contract_agent = graph.compile()