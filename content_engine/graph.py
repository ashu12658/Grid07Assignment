from langgraph.graph import StateGraph
from content_engine.nodes import decide_search, web_search, draft_post
from content_engine.state import AgentState

def build_graph():
    # Initialize state graph with AgentState schema
    builder = StateGraph(AgentState)

    # Add nodes for each step in pipeline
    builder.add_node("decide", decide_search)   # Node 1: decide search query
    builder.add_node("search", web_search)      # Node 2: perform search
    builder.add_node("draft", draft_post)       # Node 3: draft final post

    # Set entry point (first node to run)
    builder.set_entry_point("decide")

    # Define edges (execution flow between nodes)
    builder.add_edge("decide", "search")
    builder.add_edge("search", "draft")

    # Set finish point (last node to run)
    builder.set_finish_point("draft")

    # Compile graph into runnable pipeline
    return builder.compile()
