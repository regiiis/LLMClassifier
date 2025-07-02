from adapter.llm_endpoint import LLMEndpoint


class ClassifierService:
    def __init__(self, model_name: str, api_key: str):
        self.llm_adapter = LLMEndpoint(model_name=model_name, api_key=api_key)

    def classify(self, message: list, json_schema: dict = None):
        try:
            return self.llm_adapter.inference_api(message, json_schema)
        except Exception as e:
            print(f"Error during inferencing: {e}")
            return None
