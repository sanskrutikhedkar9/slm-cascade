# utils/indexer.py

import os
import chromadb
from chromadb.config import Settings
from tools.code_embedding_search import QwenAPIEmbeddingFunction


class CodeIndexer:

    def __init__(self, db_path="./chroma_db"):

        self.client = chromadb.Client(
            Settings(persist_directory=db_path)
        )

        self.embedding = QwenAPIEmbeddingFunction()

        self.collection = self.client.get_or_create_collection(
            name="codebase",
            embedding_function=self.embedding
        )


    def index_repo(self, repo_path):

        docs = []
        metadatas = []
        ids = []

        for root, _, files in os.walk(repo_path):

            for file in files:

                if file.endswith(".py"):

                    path = os.path.join(root, file)

                    with open(path, "r", encoding="utf-8") as f:

                        content = f.read()

                    docs.append(content)

                    metadatas.append({
                        "path": path
                    })

                    ids.append(path)


        print(f"Indexing {len(docs)} files")

        self.collection.add(
            documents=docs,
            metadatas=metadatas,
            ids=ids
        )

        print("Index complete")