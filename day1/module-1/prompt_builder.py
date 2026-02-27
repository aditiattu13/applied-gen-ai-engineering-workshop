from personas import PERSONAS

def build_prompt(topic, persona):
    style_rules = PERSONAS.get(persona, "")

    prompt = f"""
You are an expert educator.

Explain the following topic clearly and accurately.

Topic: {topic}

Style Instructions:
{style_rules}

Rules:
- Keep explanation factually correct
- Fully adopt the persona tone
- Make it engaging but educational
"""
    return prompt