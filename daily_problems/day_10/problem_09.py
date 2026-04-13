from typing import List, Dict


# Day 10 - Problem 9
# Topic: Time-bucket summary
#
# Each event looks like:
# {"minute": 1, "count": 5}
#
# Task:
# Return a dictionary minute -> cumulative count up to that minute in input order.
#
# Example:
# [{"minute": 1, "count": 5}, {"minute": 2, "count": 3}]
# ->
# {1: 5, 2: 8}
#
# Important:
# - use the given order
# - assume minutes are already sorted
#
# Expected output for current sample:
# {1: 5, 2: 8, 3: 10}


events = [
    {"minute": 1, "count": 5},
    {"minute": 2, "count": 3},
    {"minute": 3, "count": 2},
]


def cumulative_counts(events: List[Dict]) -> Dict[int, int]:
    minute_counts = {}
    prev_cummulative = 0
    for event in events:
        minute_counts[event["minute"]] = prev_cummulative + event["count"]
        prev_cummulative += event["count"]
    return minute_counts

if __name__ == "__main__":
    print(cumulative_counts(events))
