from typing import List, Tuple


# Day 7 - Problem 5
# Topic: Sorting + tie-break
#
# Task:
# Given a list of tuples (city, temperature), sort them by:
# - temperature descending
# - city ascending
#
# What to return:
# - the full list of tuples in sorted order
#
# Expected output for current sample:
# [("Agra", 36), ("Delhi", 36), ("Mumbai", 32), ("Pune", 29)]


temps = [
    ("Delhi", 36),
    ("Mumbai", 32),
    ("Agra", 36),
    ("Pune", 29),
]


def sort_temperatures(temps: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    sorted_cities = sorted(temps, key = lambda k: (-k[1],k[0]))
    return sorted_cities

if __name__ == "__main__":
    print(sort_temperatures(temps))
