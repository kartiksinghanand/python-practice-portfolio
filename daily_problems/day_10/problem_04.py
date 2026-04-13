from typing import List, Dict


# Day 10 - Problem 4
# Topic: Validation and reporting
#
# Task:
# Given experiment request dictionaries, return:
# {
#   "valid": <int>,
#   "invalid": <int>,
#   "modes": {"train": 2, "eval": 1, ...}
# }
#
# A request is valid only if it contains:
# - "mode"
# - "dataset"
#
# Count `modes` only for valid requests.
#
# Expected output for current sample:
# {"valid": 3, "invalid": 2, "modes": {"train": 2, "eval": 1}}


requests = [
    {"mode": "train", "dataset": "eth_small"},
    {"mode": "eval", "dataset": "eth_val"},
    {"mode": "train"},
    {},
    {"mode": "train", "dataset": "btc_small"},
]


def request_report(requests: List[Dict]) -> Dict[str, object]:
    modes = {}
    valid = 0
    invalid = 0
    for request in requests:
        keys = request.keys()
        if "mode" in keys and "dataset" in keys:
            if request["mode"] not in modes:
                modes[request["mode"]] = 1
            else:
                modes[request["mode"]] += 1
            valid += 1
        else:   
            invalid += 1
    return {"valid": valid, "invalid": invalid, "modes": modes}

if __name__ == "__main__":
    print(request_report(requests))
