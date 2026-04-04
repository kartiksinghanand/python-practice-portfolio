from typing import List, Dict


# Day 8 - Problem 8
# Topic: Feature extraction
#
# Task:
# Given records with extra fields, return a new list of dictionaries containing only:
# - "open"
# - "high"
# - "low"
# - "close"
#
# Important:
# - keep original order
# - ignore other fields
#
# What to return:
# - a new list of reduced dictionaries
#
# Expected output for current sample:
# [
#   {"open": 100, "high": 110, "low": 95, "close": 108},
#   {"open": 108, "high": 112, "low": 104, "close": 105}
# ]


records = [
    {"open": 100, "high": 110, "low": 95, "close": 108, "volume": 2000},
    {"open": 108, "high": 112, "low": 104, "close": 105, "volume": 1800},
]


def ohlc_features(records: List[Dict]) -> List[Dict]:
    # TODO
    pass


if __name__ == "__main__":
    print(ohlc_features(records))
