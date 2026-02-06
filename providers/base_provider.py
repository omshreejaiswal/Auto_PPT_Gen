class BaseLLMProvider:
    def get_available_chat_model(self):
        raise NotImplementedError

    def generate(self, prompt: str) -> str:
        raise NotImplementedError
    