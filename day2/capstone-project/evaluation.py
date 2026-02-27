from llm_layer import call_llm

def evaluate(context, question, answer):
    prompt = f"""
    Evaluate the answer based on context.

    Context:
    {context}

    Question:
    {question}

    Answer:
    {answer}

    Provide:
    - Faithfulness (0-10)
    - Relevance (0-10)
    - Hallucination Risk (Low/Medium/High)
    - Overall Score (0-10)
    """

    return call_llm(prompt, temperature=0)