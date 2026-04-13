from typing import List, Dict


# Day 9 - Problem 9
# Topic: Request batching
#
# Task:
# Given inference requests, split them into valid and invalid counts.
#
# A request is valid only if it contains:
# - "model"
# - "input"
#
# Return:
# {
#   "valid": <int>,
#   "invalid": <int>
# }
#
# Expected output for current sample:
# {"valid": 3, "invalid": 2}


requests = [
    {"model": "tiny", "input": [1, 2, 3]},
    {"model": "base"},
    {"model": "tiny", "input": [4, 5]},
    {},
    {"model": "small", "input": [9]},
]


def request_health(requests: List[Dict]) -> Dict[str, int]:
    valid = 0
    for request in requests:
        keys = request.keys()
        if "model" in keys and "input" in keys:
            valid += 1
    return {"valid" : valid, "invalid" : len(requests) - valid}


if __name__ == "__main__":
    print(request_health(requests))
