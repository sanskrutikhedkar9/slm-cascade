from utils.ast_indexer import CodeIndexer
from agents.localisation_agent import LocalizationAgent


indexer = CodeIndexer()
indexer.index_repo("sample-repo")

agent = LocalizationAgent()

results = agent.localize(
    "Fix authentication bug in login"
)

print(results)