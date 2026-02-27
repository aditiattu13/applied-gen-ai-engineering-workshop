import numpy as np
from embeddings import get_embedding

class SimpleVectorStore:
    def __init__(self):
        self.text_chunks = []
        self.embeddings = []

    def add_documents(self, chunks):
        print("Generating local embeddings...")
        for chunk in chunks:
            emb = get_embedding(chunk)
            self.text_chunks.append(chunk)
            self.embeddings.append(emb)

        self.embeddings = np.array(self.embeddings)

    def retrieve(self, query, k=5):
        query_emb = get_embedding(query)

        similarities = np.dot(self.embeddings, query_emb) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_emb)
        )

        top_k_indices = similarities.argsort()[-k:][::-1]
        return [self.text_chunks[i] for i in top_k_indices]