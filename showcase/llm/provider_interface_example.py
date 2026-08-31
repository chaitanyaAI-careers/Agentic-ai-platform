from typing import Protocol


class LLMProvider(Protocol):
    def generate(self, prompt: str) -> str:
        ...


class LocalExampleProvider:
    def generate(self, prompt: str) -> str:
        return f"Example response for: {prompt}"
