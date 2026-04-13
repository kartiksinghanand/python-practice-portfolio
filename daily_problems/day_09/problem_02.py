from typing import List, Dict


# Day 9 - Problem 2
# Topic: Feature engineering
#
# Task:
# Given daily price records, return a new list of dictionaries with only:
# - "close"
# - "range"
#
# where:
# range = high - low
#
# Important:
# - keep original order
# - return a new list, do not modify the original records
#
# Expected output for current sample:
# [
#   {"close": 108, "range": 15},
#   {"close": 105, "range": 8}
# ]


records = [
    {"open": 100, "high": 110, "low": 95, "close": 108},
    {"open": 108, "high": 112, "low": 104, "close": 105},
]


def price_features(records: List[Dict]) -> List[Dict]:
    close_range_records : List[Dict] = []
    for record in records:
        temp = {}
        temp["close"] = record["close"]
        temp["range"] = record["high"] - record["low"]
        # temp.pop("volume")
        close_range_records.append(temp)
    return close_range_records


if __name__ == "__main__":
    print(price_features(records))
