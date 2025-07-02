from ports.llm_port import LLMPort
from huggingface_hub import InferenceClient


class LLMEndpoint(LLMPort):
    """Adapter for Hugging Face LLM inference with structured JSON output."""

    def __init__(self, model_name: str, api_key: str):
        """Initialize LLM endpoint with model and API credentials.

        Args:
            model_name: Name of the model to use
            api_key: Authentication token for the API
        """
        if not model_name:
            raise ValueError("Model name must be provided.")
        if not isinstance(model_name, str):
            raise TypeError("Model name must be a string.")
        if not api_key:
            raise ValueError("API key must be provided.")
        if not isinstance(api_key, str):
            raise TypeError("API key must be a string.")
        self.model_name = model_name
        self.api_key = api_key

        try:
            self.client = InferenceClient(provider="cerebras", token=self.api_key)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to the LLM service: {e}")

    def inference_api(self, messages: list, json_schema: dict) -> dict:
        """Generate structured JSON response from chat messages.

        Args:
            messages: List of chat messages with role and content
            json_schema: JSON schema to enforce response structure

        Returns:
            Parsed JSON response as dictionary
        """
        if not messages:
            raise ValueError("Messages must be provided for inference.")
        if not isinstance(messages, list):
            raise TypeError("Messages must be a list.")
        if not json_schema:
            raise ValueError("JSON schema must be provided for inference.")
        if not isinstance(json_schema, dict):
            raise TypeError("JSON schema must be a dictionary.")

        formatted_schema = {
            "name": "classification",
            "schema": json_schema,
            "strict": True,
        }

        try:
            completion = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                response_format={
                    "type": "json_schema",
                    "json_schema": formatted_schema,
                },
            )
        except Exception as e:
            raise RuntimeError(f"Error during inference: {e}")

        return completion
