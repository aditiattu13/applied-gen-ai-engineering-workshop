import streamlit as st
from litellm import completion
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

st.set_page_config(page_title="Text Explainer", layout="wide")
st.title("🧠 AI Research paper Explainer")

input_text = st.text_area("📄 Paste your text here:", height=300)
question = st.text_input("❓ What do you want to know about it?")

def call_llm(prompt):
    response = completion(
        model="groq/llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]

if st.button("Explain"):
    if input_text and question:
        with st.spinner("Thinking..."):
            prompt = f"""
You are an academic assistant.

Text:
{input_text}

User Question:
{question}

Answer clearly and in simple language.
"""
            answer = call_llm(prompt)

        st.subheader("📝 Answer:")
        st.write(answer)
    else:
        st.warning("Please paste text and enter a question.")