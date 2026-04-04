from typing import List, Dict


# Day 8 - Problem 10
# Topic: Product-style AI prep task
#
# Task:
# Given prediction results, return:
# {
#   "total_predictions": <int>,
#   "above_threshold": <int>,
#   "avg_score": <float>
# }
#
# Rules:
# - threshold = 0.70
# - above_threshold counts scores >= 0.70
# - avg_score = average of all scores
# - if input is empty, avg_score should be 0.0
#
# What to return:
# - a summary dictionary with the three fields above
#
# Expected output for current sample:
# {"total_predictions": 4, "above_threshold": 2, "avg_score": 0.625}


predictions = [
    {"id": "P1", "score": 0.91},
    {"id": "P2", "score": 0.43},
    {"id": "P3", "score": 0.70},
    {"id": "P4", "score": 0.46},
]


def prediction_summary(predictions: List[Dict]) -> Dict[str, float]:
    # TODO
    pass


if __name__ == "__main__":
    print(prediction_summary(predictions))
