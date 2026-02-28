import chromadb
from chromadb.config import Settings

from tools.code_embedding_search import QwenAPIEmbeddingFunction


class CodeIndexer:

    def __init__(self):

        self.client = chromadb.Client(
            Settings(persist_directory="./chroma_db")
        )

        self.embedding = QwenAPIEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="codebase",
            embedding_function=self.embedding
        )


    def add_chunk(self, id, text, metadata):

        self.collection.add(
            ids=[id],
            documents=[text],
            metadatas=[metadata]
        )