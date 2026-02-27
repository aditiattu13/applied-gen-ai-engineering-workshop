from llm_layer import call_llm

def detect_intent(query):
    prompt = f"""
    Classify the query:
    summarize | explain | compare | generate_questions

    Query: {query}

    Return only the category name.
    """
    return call_llm(prompt).strip().lower()

def agent_reasoning(vectorstore, query):

    intent = detect_intent(query)

    context_chunks = vectorstore.retrieve(query)
    context = "\n\n".join(context_chunks)

    if "summarize" in intent:
        instruction = "Summarize clearly in bullet points."
    elif "explain" in intent:
        instruction = "Explain in simple beginner-friendly language."
    elif "compare" in intent:
        instruction = "Provide structured comparison."
    elif "generate_questions" in intent:
        instruction = "Generate 5 viva questions with answers."
    else:
        instruction = "Answer clearly and accurately."

    final_prompt = f"""
    You are a Research Paper Explainer AI.

    Context:
    {context}

    Question:
    {query}

    Task:
    {instruction}
    """

    return call_llm(final_prompt)