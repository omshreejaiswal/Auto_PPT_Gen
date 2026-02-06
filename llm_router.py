from providers.groq_provider import GroqProvider
from providers.openai_provider import OpenAIProvider
from providers.anthropic_provider import AnthropicProvider
from providers.gemini_provider import GeminiProvider
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_llm(provider_name, api_key):
    if provider_name == "Groq":
        return GroqProvider(api_key)
    if provider_name == "OpenAI":
        return OpenAIProvider(api_key)
    if provider_name == "Anthropic":
        return AnthropicProvider(api_key)
    if provider_name == "Gemini":
        return GeminiProvider(api_key)
    raise ValueError("Unsupported LLM provider")