from sentence_transformers import SentenceTransformer
from chromadb.api.types import EmbeddingFunction
import numpy as np


class QwenEmbeddingFunction(EmbeddingFunction):

    def __init__(self):

        print("Loading Qwen embedding model...")

        self.model = SentenceTransformer(
            "Qwen/Qwen3-Embedding-0.6B",
            device="cpu"   # or "cuda"
        )

        print("Model loaded")


    def __call__(self, texts):

        if isinstance(texts, str):
            texts = [texts]

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return embeddings.tolist()