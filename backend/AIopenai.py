from AI import AI

class AIopenai(AI):
    def __init__(self, *args, **kwargs):
        pass

    def call(self, *args, **kwargs):
        return "OpenAI"

    def local_test(self):
        return "OpenAI"