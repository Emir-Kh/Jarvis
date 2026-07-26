from brain.conversation import conversation
from brain.prompts import build_messages

from brain.llm_client import LLMClient

class AIManager:

    def __init__(self):

        self.client = LLMClient()

    def ask(self, text):

        conversation.add("user", text)

        messages = build_messages(
            text,
            conversation.history()
        )

        response = self.client.ask(messages)

        conversation.add(
            "assistant",
            response
        )

        return response