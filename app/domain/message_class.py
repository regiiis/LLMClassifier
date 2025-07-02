from typing import List


def create_messages_from_feedbacks(feedbacks: List[str]) -> List[List[dict]]:
    """Create a list of message sets from a list of feedbacks.

    Args:
        feedbacks: List of customer feedback strings

    Returns:
        List of message sets, each containing system and user messages
        formatted for LLM classification
    """
    message_sets = []
    for feedback in feedbacks:
        message_set = [
            {
                "role": "system",
                "content": "Extract the issue type, severity, and problem summary from the following customer review.",
            },
            {"role": "user", "content": feedback},
        ]
        message_sets.append(message_set)

    return message_sets
