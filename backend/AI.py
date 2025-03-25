import json
import os
from abc import ABC, abstractmethod


class AI(ABC):
    class Conversation:
        def __init__(self, save_path, filename):
            self.messages = []
            self.summary = None
            self.summarized_to = 0
            self.save_path = save_path
            self.filename = filename
            os.makedirs(self.save_path, exist_ok=True)  # Create directory if it doesn't exist
            self.load()  # load the conversation when initialized.

        def add_message(self, role, content):
            self.messages.append({"role": role, "content": content})

        def get_messages(self):
            if self.summary:
                return [{"role": "system", "content": self.summary}] + self.messages[self.summarized_to:]

        def set_summary(self, summary, summarized_to):
            self.summary = summary
            self.summarized_to = summarized_to

        def save(self):
            filepath = os.path.join(self.save_path, self.filename)
            data = {
                "messages": self.messages,
                "summary": self.summary,
                "summarized_to": self.summarized_to,
            }
            with open(filepath, "w") as f:
                json.dump(data, f)

        def load(self):
            filepath = os.path.join(self.save_path, self.filename)
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                self.messages = data.get("messages", [])
                self.summary = data.get("summary", None)
                self.summarized_to = data.get("summarized_to", None)
            except FileNotFoundError:
                print(f"Conversation file '{self.filename}' not found. Creating a new one.")
                self.save()  # create an empty save file.
            except json.JSONDecodeError:
                print(f"Error decoding JSON from '{self.filename}'. Creating a new empty file.")
                self.save()  # create an empty save file.

        def clear(self):
            self.messages = []
            self.summary = None
            self.summarized_to = None
            self.save()  # save the cleared conversation.

        def __repr__(self):
            return f"Conversation(messages={self.messages}, summary={self.summary}, summarized_to={self.summarized_to})"

    def __init__(self, *args, **kwargs):
        self.api_key = None
        self.client = None
        self.model = None
        self.conversation = None

    @abstractmethod
    def call(self, *args, **kwargs):
        pass

    @abstractmethod
    def local_test(self, *args, **kwargs):
        pass
