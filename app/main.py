import os
import json
from domain.classifier import ClassifierService
from domain.message_class import create_messages_from_feedbacks

schema_path = "data/customer_feedback_json_schema.json"
feedbacks_path = "data/feedbacks_google.json"
model_name = "Qwen/Qwen3-32B"


class classifier:
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def _load_json_schema(self, schema_path: str):
        """Load JSON schema from a file."""
        try:
            with open(schema_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"Schema file not found: {schema_path}")

    def _load_feedbacks_list(self, feedbacks_path: str):
        """Load feedbacks from JSON file."""
        if not feedbacks_path:
            raise ValueError("feedbacks path must be provided.")
        if not isinstance(feedbacks_path, str):
            raise TypeError("feedbacks path must be a string.")

        try:
            with open(feedbacks_path, "r", encoding="utf-8") as file:
                feedbacks = json.load(file)

            # Validate that it's a list of strings
            if not isinstance(feedbacks, list):
                raise TypeError("JSON file must contain an array of strings.")

            # Filter out empty or invalid entries
            valid_feedbacks = []
            for feedback in feedbacks:
                if isinstance(feedback, str) and feedback.strip():
                    valid_feedbacks.append(feedback.strip())

            return valid_feedbacks

        except FileNotFoundError:
            raise ValueError(f"feedbacks file not found: {feedbacks_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in feedbacks file: {e}")
        except Exception as e:
            raise RuntimeError(f"Error reading feedbacks file: {e}")

    def _run_classification(self, message: list):
        json_schema = self._load_json_schema(schema_path)
        if not json_schema:
            raise ValueError("JSON schema is empty or not loaded correctly.")
        if not isinstance(json_schema, dict):
            raise TypeError("JSON schema must be a dictionary.")

        classifier_service = ClassifierService(
            model_name=self.model_name, api_key=self.api_key
        )
        result = classifier_service.classify(message=message, json_schema=json_schema)
        return result

    def loop_feedbacks(self, feedbacks_path: str):
        """Loop through feedbacks and classify each one."""
        feedbacks = self._load_feedbacks_list(feedbacks_path)
        if not feedbacks:
            raise ValueError("feedbacks list is empty.")

        # Use your message_class function
        message_sets = create_messages_from_feedbacks(feedbacks)

        results = []
        for message in message_sets:
            classification_result = self._run_classification(message)
            if classification_result:
                results.append(classification_result)

        return results


if __name__ == "__main__":
    print(f"\nRunning classification with model: {model_name}\n")
    api_key = os.getenv("ACCESS_TOKEN")

    classifier_instance = classifier(model_name=model_name, api_key=api_key)
    classification_results = classifier_instance.loop_feedbacks(feedbacks_path)

    print(f"\nProcessed {len(classification_results)} feedbacks")
    for i, result in enumerate(classification_results):
        print(f"\nFeedback {i + 1}: {result.choices[0].message}")
