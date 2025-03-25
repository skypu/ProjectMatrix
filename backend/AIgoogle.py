import os

from google import genai

from AI import AI


class AIgoogle(AI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_key = os.getenv("GOOGLE_API_KEY")

        self.client = genai.Client(api_key=self.api_key)

        self.model = kwargs.get("model", "")

        self.conversation = AI.Conversation(save_path=kwargs.get("memory_path", "conversations"),
                                            filename=kwargs.get("memory_name", "conversation.json"))

    def call(self, *args, **kwargs):
        prompt = kwargs.get("prompt", "hello world")
        response = self.client.models.generate_content(
            model=self.model, contents=prompt
        )
        return response

    def local_test(self, *args, **kwargs):
        self.call(prompt="hello, world")
        return "Google"


if __name__ == "__main__":
    ai = AIgoogle()
    ai.local_test()
