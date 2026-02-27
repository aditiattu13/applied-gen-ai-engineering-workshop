import streamlit as st
from prompt_builder import build_prompt
from llm_interface import generate_response

st.set_page_config(page_title="PersonaPrompt AI", page_icon="🎭")

st.title("🎭 PersonaPrompt: Multi-Audience AI Explainer")

st.markdown("Enter a complex topic and choose a persona style.")

topic = st.text_input("📘 Enter Topic")

persona = st.selectbox(
    "🎭 Choose Persona",
    ["Shakespeare", "Pirate", "Cowboy"]
)

col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("Generate Explanation")

with col2:
    compare_btn = st.button("Compare All Personas")

if generate_btn and topic:
    with st.spinner("Generating explanation..."):
        prompt = build_prompt(topic, persona)
        response = generate_response(prompt)

    st.subheader(f"Explanation in {persona} Mode")
    st.write(response)

elif compare_btn and topic:
    st.subheader("Persona Comparison")

    for p in ["Shakespeare", "Pirate", "Cowboy"]:
        with st.spinner(f"Generating {p} version..."):
            prompt = build_prompt(topic, p)
            response = generate_response(prompt)

        st.markdown(f"### 🎭 {p}")
        st.write(response)
        st.divider()

elif (generate_btn or compare_btn) and not topic:
    st.warning("Please enter a topic first.")