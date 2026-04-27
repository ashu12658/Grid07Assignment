from sentence_transformers import SentenceTransformer

# Load lightweight MiniLM model for text embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    # Encode input text into normalized embedding vector
    return model.encode(text, normalize_embeddings=True)
