from openai import OpenAI
from providers.base_provider import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.model = self.get_available_chat_model()

    def get_available_chat_model(self):
        candidate_models = ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
        for model in candidate_models:
            try:
                self.client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": "ping"}],
                    max_tokens=1
                )
                return model
            except Exception:
                continue
        raise RuntimeError("No OpenAI model available for this API key")

    def generate(self, prompt):
        res = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )
        return res.choices[0].message.content