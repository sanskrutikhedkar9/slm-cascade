# agents/localisation_agent.py

import chromadb
from chromadb.config import Settings
from client.qwen_embed import QwenEmbeddingFunction


class LocalizationAgent:

    def __init__(self):

        client = chromadb.Client(
            Settings(persist_directory="./chroma_db")
        )

        embedding = QwenEmbeddingFunction()

        self.collection = client.get_collection(
            name="codebase",
            embedding_function=embedding
        )


    def localize(self, issue):

        query = f"""
        Instruct: Retrieve code relevant to fixing this bug
        Query: {issue}
        """

        results = self.collection.query(
            query_texts=[query],
            n_results=5
        )

        return results