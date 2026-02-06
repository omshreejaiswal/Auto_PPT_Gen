import google.generativeai as genai
from providers.base_provider import BaseLLMProvider

class GeminiProvider(BaseLLMProvider):
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = self.get_available_chat_model()

    def get_available_chat_model(self):
        candidate_models = [
            "gemini-1.5-flash",
            "gemini-1.5-pro",
            "gemini-pro"
        ]
        for name in candidate_models:
            try:
                model = genai.GenerativeModel(name)
                model.generate_content("ping")
                return name
            except Exception:
                continue
        raise RuntimeError("No Gemini model available for this API key")

    def generate(self, prompt):
        model = genai.GenerativeModel(self.model)
        return model.generate_content(prompt).text