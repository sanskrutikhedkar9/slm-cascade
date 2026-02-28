# utils/indexer.py

import os
import chromadb
from chromadb.config import Settings
from client.qwen_embed import QwenEmbeddingFunction
from utils.ast_chunker import extract_code_chunks


class CodeIndexer:

    def __init__(self):

        self.client = chromadb.Client(
            Settings(persist_directory="./chroma_db")
        )

        self.embedding = QwenEmbeddingFunction()

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

                    chunks = extract_code_chunks(path)
                    
                    for chunk in chunks:

                        docs.append(chunk["code"])

                        metadatas.append({
                            "path": chunk["path"],
                            "name": chunk["name"],
                            "type": chunk["type"],
                            "start": chunk["start"],
                            "end": chunk["end"]
                        })

                        ids.append(f"{path}:{chunk['name']}")
        print(f"Indexing {len(docs)} functions")

        self.collection.add(
            documents=docs,
            metadatas=metadatas,
            ids=ids
        )

        print("Index complete")