# Load environment variables (API keys, configs etc.)
from dotenv import load_dotenv

load_dotenv()

# Import helper functions from Combat Engine
from combat_engine.prompt import build_defense_prompt  # Builds persona + defense prompt
from combat_engine.rag_utils import merge_thread_context  # Merges thread context for RAG
from langchain_groq import ChatGroq


def generate_defense_reply(bot_persona, parent_post, comment_history, human_reply):
    # Merge all thread context (parent post + history + latest reply)
    context = merge_thread_context(human_reply, parent_post, comment_history)

    # Build defense prompt using persona + context
    prompt = build_defense_prompt(bot_persona, context)

    # Initialize Groq LLM (Llama‑3.3‑70B versatile model)
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    # Generate reply from LLM
    reply = llm.invoke(prompt)

    return reply
