from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ['git_token']
)

response = client.chat.completions.create(
    model="microsoft/phi-3-mini-4k-instruct",
    messages=[
        {"role": "user", "content": "Explain quicksort in simple words"}
    ]
)

print(response.choices[0].message.content)