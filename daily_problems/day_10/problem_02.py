from typing import List, Tuple


# Day 10 - Problem 2
# Topic: Sorting with multiple priorities
#
# Task:
# Given a list of tuples (model_name, latency_ms, accuracy),
# sort by:
# - accuracy descending
# - latency ascending
# - model_name ascending
#
# Expected output for current sample:
# [("tiny_b", 0.91, 80), ("base_a", 0.91, 90), ("small_x", 0.88, 70), ("zero_q", 0.88, 90)]


models = [
    ("base_a", 90, 0.91),
    ("tiny_b", 80, 0.91),
    ("small_x", 70, 0.88),
    ("zero_q", 90, 0.88),
]


def rank_models(models: List[Tuple[str, int, float]]) -> List[Tuple[str, float, int]]:
    return sorted(models, key = lambda k: (-k[2],k[1],k[0]))


if __name__ == "__main__":
    print(rank_models(models))
