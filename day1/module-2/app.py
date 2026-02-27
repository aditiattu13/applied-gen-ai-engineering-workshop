import streamlit as st
from prompt_builder import build_prompt
from llm_interface import generate_response

st.set_page_config(page_title="Structured Answer Generator", page_icon="📚")

st.title("📚 Structured Answer Generator")
st.markdown("Generate academically structured answers using AI.")

question = st.text_area("Enter your Question")

answer_length = st.selectbox(
    "Select Answer Length",
    ["Short (5 Marks)", "Medium (10 Marks)", "Long (15+ Marks)"]
)

if st.button("Generate Structured Answer"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating structured answer..."):
            prompt = build_prompt(question, answer_length)
            answer = generate_response(prompt)

        st.subheader("📄 Generated Answer")
        st.write(answer)