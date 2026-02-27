from config import STRUCTURE_TEMPLATE

def build_prompt(question, answer_length):

    length_instruction = {
        "Short (5 Marks)": "Keep explanation concise (150-200 words).",
        "Medium (10 Marks)": "Provide moderate detail (300-400 words).",
        "Long (15+ Marks)": "Provide in-depth explanation (600+ words)."
    }

    prompt = f"""
You are an academic expert.

Question:
{question}

{STRUCTURE_TEMPLATE}

Additional Instructions:
{length_instruction.get(answer_length, "")}

Rules:
- Follow the structure exactly.
- Do not skip any section.
- Do not add extra sections.
- Maintain professional academic tone.
"""

    return prompt