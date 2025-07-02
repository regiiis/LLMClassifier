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
                "content": "Analyze the customer review and extract structured information. Classify the feedback type (Positive/Negative/Neutral/Mixed), identify issue types and compliment types (can be multiple from: Treatment, Communication, Staff_Behavior, Facilities, Administrative, Safety, Wait_Times, Other, None), assess severity level (low/medium/high/None), and provide, rather short, both negative and positive summaries where applicable.",
            },
            {"role": "user", "content": feedback},
        ]
        message_sets.append(message_set)

    return message_sets
