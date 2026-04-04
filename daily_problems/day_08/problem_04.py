from typing import List, Dict


# Day 8 - Problem 4
# Topic: Config parsing
#
# Each line looks like:
# "learning_rate=0.001"
#
# Task:
# Parse config lines into one dictionary.
#
# Important:
# - ignore malformed lines only
# - keep values as strings for this problem
# - return {} for empty input
#
# What to return:
# - one dictionary of config key/value pairs
#
# Expected output for current sample:
# {"learning_rate": "0.001", "epochs": "10", "model": "tiny-transformer"}


lines = [
    "learning_rate=0.001",
    "epochs=10",
    "model=tiny-transformer",
    "badline",
]


def parse_config(lines: List[str]) -> Dict[str, str]:
    # TODO
    pass


if __name__ == "__main__":
    print(parse_config(lines))
