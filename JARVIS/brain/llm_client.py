import ollama


class LLMClient:

    def __init__(self):

        self.model = "llama3.2"

    def ask(self, messages):

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]