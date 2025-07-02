import os
from domain.classifier import ClassifierService

model_name = "Qwen/Qwen3-32B"
json_schema = {
    "type": "object",
    "properties": {
        "issue_type": {
            "type": "string",
            "enum": [
                "Treatment",
                "Communication",
                "Staff_Behavior",
                "Facilities",
                "Administrative",
                "Safety",
                "Wait_Times",
                "Other",
            ],
        },
        "severity": {"type": "string", "enum": ["low", "medium", "high"]},
        "problem_summary": {"type": "string"},
    },
    "required": ["issue_type", "severity", "problem_summary"],
}

message = [
    {
        "role": "system",
        "content": "Extract the issue type, severity, and problem summary from the following customer review.",
    },
    {
        "role": "user",
        "content": "They took a coffee break during the op. Anesthesia started wearing off and I felt everything. Worst day of my life.",
    },
]


class classifier:
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def run_classification(self):
        classifier_service = ClassifierService(
            model_name=self.model_name, api_key=self.api_key
        )
        result = classifier_service.classify(message=message, json_schema=json_schema)
        return result


if __name__ == "__main__":
    print(f"\nRunning classification with model: {model_name}\n")
    api_key = os.getenv("ACCESS_TOKEN")
    classifier_instance = classifier(model_name=model_name, api_key=api_key)
    classification_result = classifier_instance.run_classification()
    print(f"\nClassification result: {classification_result}")
