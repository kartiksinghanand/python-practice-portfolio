from typing import List, Dict


# Day 9 - Problem 1
# Topic: Time-series preprocessing
#
# Task:
# Given daily price records, return a list containing only the closing prices.
#
# Important:
# - keep original order
# - return [] for empty input
#
# What to return:
# - a list of close values only
#
# Expected output for current sample:
# [108, 105, 111]


records = [
    {"open": 100, "high": 110, "low": 95, "close": 108},
    {"open": 108, "high": 112, "low": 104, "close": 105},
    {"open": 105, "high": 115, "low": 102, "close": 111},
    {"open": 110, "high": 116, "low": 100, "close": 115},
    {"open": 150, "high": 119, "low": 98, "close": 120},
    {"open": 180, "high": 120, "low": 103, "close": 130},
]


def closing_prices(records: List[Dict]) -> List[int]:
    close_values = []
    for record in records:
        close_values.append( record["close"])
    return close_values

if __name__ == "__main__":
    print(closing_prices(records))
