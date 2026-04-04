from typing import List, Dict


# Day 8 - Problem 9
# Topic: Inference request validation
#
# Task:
# Given inference request dictionaries, return:
# {
#   "valid_requests": <int>,
#   "invalid_requests": <int>,
#   "model_usage": {"tiny": 2, "base": 1, ...}
# }
#
# A request is valid only if it contains:
# - "model"
# - "prompt"
#
# Important:
# - count model_usage only for valid requests
# - ignore malformed requests safely
#
# Expected output for current sample:
# {"valid_requests": 3, "invalid_requests": 2, "model_usage": {"tiny": 2, "base": 1}}


requests = [
    {"model": "tiny", "prompt": "hello"},
    {"model": "base", "prompt": "summarize this"},
    {"model": "tiny"},
    {},
    {"model": "tiny", "prompt": "forecast"},
]


def inference_summary(requests: List[Dict]) -> Dict[str, object]:
    # TODO
    pass


if __name__ == "__main__":
    print(inference_summary(requests))
