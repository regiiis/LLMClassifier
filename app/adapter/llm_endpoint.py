from ports.llm_port import LLMPort
from huggingface_hub import InferenceClient


class LLMEndpoint(LLMPort):
    def __init__(self, model_name: str, api_key: str):
        if not model_name:
            raise ValueError("Model name must be provided.")
        if not api_key:
            raise ValueError("API key must be provided.")
        if not isinstance(model_name, str):
            raise TypeError("Model name must be a string.")
        if not isinstance(api_key, str):
            raise TypeError("API key must be a string.")
        self.model_name = model_name
        self.api_key = api_key
        self.client = InferenceClient(provider="cerebras", token=self.api_key)

    def inference_api(self, messages: list, json_schema: dict) -> dict:
        print(f"LLM Messages: {messages}\n")

        # Format the JSON schema properly for Cerebras API
        formatted_schema = {
            "name": "classification",
            "schema": json_schema,
            "strict": True,
        }

        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": formatted_schema,  # Use the properly formatted schema
            },
        )
        print(f"LLM Completion: {completion}")
        return completion.choices[0].message
