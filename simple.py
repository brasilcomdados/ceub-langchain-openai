# pip install openai - NAO INSTALAR
from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', default='')
OPENAI_ORGANIZATION = os.getenv("OPENAI_ORGANIZATION")

llm = OpenAI(api_key=OPENAI_API_KEY, openai_organization=OPENAI_ORGANIZATION)

for chunk in llm.stream(
        "Quais são os riscos entre o desemprego e a inflação no Brasil?"
):
    print(chunk, end="", flush=True)
