from groq import Groq
from providers.base_provider import BaseLLMProvider


class GroqProvider(BaseLLMProvider):
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = self.get_available_chat_model()

    def get_available_chat_model(self):
        models = self.client.models.list()

        for m in models.data:
            model_id = m.id.lower()

            # STRICT filtering: ONLY chat-capable LLMs
            if (
                ("llama" in model_id or "mixtral" in model_id or "gemma" in model_id)
                and "whisper" not in model_id
                and "audio" not in model_id
                and "speech" not in model_id
            ):
                return m.id

        # NO FALLBACK TO NON-CHAT MODELS
        raise RuntimeError("No chat-capable Groq model available")

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.4
        )
        return response.choices[0].message.content