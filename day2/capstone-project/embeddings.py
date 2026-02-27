import numpy as np
from sentence_transformers import SentenceTransformer

# Load once globally
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    return np.array(model.encode(text))