import json
from content_engine.llm import generate_post, generate_query
from content_engine.tools import mock_searxng_search


def decide_search(state):
    # Extract persona from state
    persona = state["persona"]
    # Generate a search query based on persona
    query = generate_query(persona)
    # Return updated state with query added
    return {**state, "query": query}


def web_search(state):
    # Get query from state
    query = state["query"]

    # Direct tool call to mock search (avoids LLM confusion)
    results = mock_searxng_search.invoke({"query": query})

    # Return updated state with search results
    return {
        **state,
        "results": results
    }


def draft_post(state):
    # Extract required fields from state
    persona = state["persona"]
    results = state["results"]
    bot_id = state["bot_id"]
    topic = state["query"]

    # Generate raw post output using LLM
    raw_output = generate_post(persona, results, topic, bot_id)

    try:
        # Try parsing output as JSON
        parsed = json.loads(raw_output)
    except Exception:
        # Fallback if JSON parsing fails
        print("⚠️ JSON parse failed, fallback used.")
        parsed = {
            "bot_id": bot_id,
            "topic": topic,
            "post_content": raw_output or "LLM returned empty output"
        }

    # Return final structured post
    return {
        "bot_id": parsed["bot_id"],
        "topic": parsed["topic"],
        "post_content": parsed["post_content"]
    }
