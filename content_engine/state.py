
from typing import TypedDict

class AgentState(TypedDict, total=False):
    bot_id: str
    persona: str
    query: str
    results: str
    topic: str
    post_content: str