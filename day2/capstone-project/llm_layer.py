import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

MODEL = "groq/llama-3.1-8b-instant"

def call_llm(prompt, temperature=0.2):
    response = completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        api_key=os.getenv("GROQ_API_KEY")
    )
    return response["choices"][0]["message"]["content"]