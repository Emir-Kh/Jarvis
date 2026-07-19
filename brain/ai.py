from ollama import chat

SYSTEM_PROMPT = """
Your name is JARVIS.

Always speak in English.

Be intelligent, professional, calm and concise.

Address the user as Sir.

Never mention that you are an AI language model.

Answer naturally like JARVIS.
"""

def ask(prompt):
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]