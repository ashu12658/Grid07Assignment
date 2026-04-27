from langchain.tools import tool

@tool("mock_searxng_search", return_direct=True)
def mock_searxng_search(query: str) -> str:
    """
    A mock search tool that returns hardcoded recent news headlines
    based on keywords. Used for Phase 2 of the assignment.
    """
    query_lower = query.lower()
    if "crypto" in query_lower:
        return "Bitcoin hits new all-time high amid regulatory ETF approvals."
    elif "ai" in query_lower:
        return "OpenAI releases new multimodal model capable of reasoning across text and images."
    elif "space" in query_lower:
        return "SpaceX successfully launches next-gen Starlink satellites."
    elif "finance" in query_lower:
        return "Global markets rally as interest rates stabilize."
    else:
        return "No relevant news found for the given query."
