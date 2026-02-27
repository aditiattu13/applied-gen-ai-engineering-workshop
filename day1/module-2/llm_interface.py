import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

def generate_response(prompt):
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a structured academic answer generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,  # lower for structured consistency
        max_tokens=1000
    )

    return response["choices"][0]["message"]["content"]