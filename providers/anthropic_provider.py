import anthropic
from providers.base_provider import BaseLLMProvider

class AnthropicProvider(BaseLLMProvider):
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = self.get_available_chat_model()

    def get_available_chat_model(self):
        candidate_models = [
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229",
            "claude-3-opus-20240229"
        ]
        for model in candidate_models:
            try:
                self.client.messages.create(
                    model=model,
                    messages=[{"role": "user", "content": "ping"}],
                    max_tokens=1
                )
                return model
            except Exception:
                continue
        raise RuntimeError("No Anthropic model available for this API key")

    def generate(self, prompt):
        msg = self.client.messages.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )
        return msg.content[0].text