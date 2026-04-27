from dotenv import load_dotenv
load_dotenv()
from router.vector_store import search_similar
from content_engine.llm import model


def preprocess_post(post: str):
    # Build a prompt to extract 5 specific keywords from the post
    prompt = f"""
Extract ONLY 5 highly relevant and specific keywords from the text.

Text: {post}

Rules:
- Focus on main topic only
- Avoid generic AI terms unless necessary
- Keep it concise

Output format:
Topics: keyword1, keyword2, keyword3, keyword4, keyword5
"""

    # Send prompt to LLM
    response = model.invoke(prompt)
    content = (response.content or "").strip()

    # Ensure output starts with "Topics:" prefix
    return content if content.startswith("Topics:") else f"Topics: {content}"


def route_post_to_bots(post_content: str, threshold: float = 0.35):
    # Preprocess post before embedding (extract keywords first)
    processed_post = preprocess_post(post_content)

    # Search for similar personas using vector store
    scores, indices, personas = search_similar(processed_post)
    persona_keys = list(personas.keys())

    matched_bots = []

    # Adaptive threshold logic
    effective_threshold = threshold
    if max(scores) < threshold:
        effective_threshold = max(scores) - 0.01

    # Iterate over scores and match bots above threshold
    for i, score in zip(indices, scores):
        print(f"{persona_keys[i]} → score: {score:.2f}")
        if score >= effective_threshold:
            matched_bots.append(persona_keys[i])

    # Return list of matched bot IDs
    return matched_bots
