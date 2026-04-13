from typing import List, Dict


# Day 9 - Problem 4
# Topic: Config validation
#
# Task:
# Given config dictionaries, return the count of valid configs.
#
# A config is valid only if it contains:
# - "model"
# - "learning_rate"
# - "epochs"
#
# Important:
# - count valid configs only
# - ignore incomplete configs
#
# Expected output for current sample:
# 2


configs = [
    {"model": "tiny", "learning_rate": 0.001, "epochs": 10},
    {"model": "base", "epochs": 20},
    {"model": "small", "learning_rate": 0.0005, "epochs": 15},
]


def valid_config_count(configs: List[Dict]) -> int:
    valid = 0
    for config in configs:
        keys = config.keys()
        if "model" in keys and "learning_rate" in keys and "epochs" in keys:
            valid += 1
            # print("Keys: ", keys)
    return valid

if __name__ == "__main__":
    print(valid_config_count(configs))
