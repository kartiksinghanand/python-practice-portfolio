from typing import List


# Day 3 - Problem 2
# Topic: Functions + edge cases
#
# Task:
# Write a function normalize_temperatures(values) that:
# 1) Removes None values
# 2) Converts remaining values to float
# 3) Returns a new list rounded to 1 decimal place
#
# Example:
# [36, "37.26", None, 38.0] -> [36.0, 37.3, 38.0]
#
# Requirements:
# - Return [] for empty input
# - Ignore invalid values safely using try/except


def normalize_temperatures(values: List[object]) -> List[float]:
    
    normalize_temp_list = []
    for temp in values:
        if temp == None:
            continue    
        try:
            value = float(temp)
            normalize_temp_list.append(round(value,1))
        except:
            continue
    
    return normalize_temp_list


if __name__ == "__main__":
    tests = [
        [36, "37.26", None, 38.0],
        ["bad", None, "40.55", 39],
        [],
    ]

    for t in tests:
        print(t, "->", normalize_temperatures(t))
