import json
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

#  Initialize Groq model with tool binding
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)


#  Generate post using persona + context
def generate_post(persona, context, topic, bot_id):
    prompt = f"""
You are a bot with this persona:
{persona}

You have already used the search tool and found this context:
{context}

Now write a highly opinionated Twitter-style post (max 280 chars)
based on the topic "{topic}" and your persona's beliefs.

Return STRICT JSON ONLY:
{{
  "bot_id": "{bot_id}",
  "topic": "{topic}",
  "post_content": "..."
}}
"""
    response = model.invoke(prompt)
    content = (response.content or "").strip()

    # Fallback if model gives non-JSON or empty output
    if not content.startswith("{"):
        content = json.dumps({
            "bot_id": bot_id,
            "topic": topic,
            "post_content": content[:280] or "No content generated"
        })

    return content


# 🔹 Generate query using persona
def generate_query(persona):
    prompt = f"""
You are a bot with this persona:
{persona}

Generate a detailed search query for retrieving relevant information.

IMPORTANT:
- Output MUST be a structured topic representation
- Include domain-specific keywords
- Use this exact format:

{{
  "query": "Topics: <comma separated keywords>"
}}

Example:
"Topics: artificial intelligence, OpenAI, automation, job displacement, software development"

DO NOT return a short phrase like "AI news"
DO NOT call any tool
Return STRICT JSON ONLY
"""
    response = model.invoke(prompt)
    content = (response.content or "").strip()

    print("RAW QUERY OUTPUT:", content)

    try:
        parsed = json.loads(content)
        return parsed["query"]
    except Exception:
        return f"Topics: {content.replace('"', '').strip()}"