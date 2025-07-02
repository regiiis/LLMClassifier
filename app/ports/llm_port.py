from abc import ABC, abstractmethod


class LLMPort(ABC):
    @abstractmethod
    def inference_api(self, messages: list, json_schema: dict) -> dict:
        """Method to perform inference using the LLM."""
        pass
