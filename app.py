from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("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")
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain artificial intelligence in one simple paragraph."
)

print(response.output_text)