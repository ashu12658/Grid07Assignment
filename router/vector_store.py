import faiss
import numpy as np
from router.embeddings import get_embedding

# Personas
personas = {
    "A": "I believe AI and crypto will solve all human problems...",
    "B": "I believe late-stage capitalism is destroying society...",
    "C": "I care about markets, trading, ROI..."
}

# Create embeddings
persona_texts = list(personas.values())
persona_embeddings = np.array([get_embedding(text) for text in persona_texts],dtype="float32")

# FAISS index
dimension = persona_embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

index.add(persona_embeddings)

def search_similar(post: str, k=3):
    post_embedding = np.array([get_embedding(post)],dtype="float32")
    distances, indices = index.search(post_embedding, k)
    return distances[0], indices[0], personas