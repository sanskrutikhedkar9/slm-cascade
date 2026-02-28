#find file based on file embedding and issue embedding

# agent/localization/embedding.py

from huggingface_hub import InferenceClient
from chromadb.api.types import EmbeddingFunction, Documents, Embeddings
import os
from dotenv import load_dotenv
load_dotenv()


class QwenAPIEmbeddingFunction(EmbeddingFunction):

    def __init__(self):

        self.client = InferenceClient(
            token=os.environ['HF_TOKEN']
        )

    def embed(self, texts):

        if isinstance(texts, str):
            texts = [texts]

        embeddings = []

        for text in texts:

            emb = self.client.feature_extraction(text, model="Qwen/Qwen3-Embedding-0.6B")

            embeddings.append(emb)

        return embeddings


    def __call__(self, input: Documents) -> Embeddings:

        return self.embed(input)