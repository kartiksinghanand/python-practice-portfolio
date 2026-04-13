from typing import List, Dict, Tuple


# Day 9 - Problem 5
# Topic: Ranking
#
# Task:
# Given model scores, return a sorted leaderboard as:
# [(model_name, score), ...]
#
# Sort by:
# - score descending
# - model name ascending
#
# Expected output for current sample:
# [("base", 0.91), ("tiny", 0.88), ("zero", 0.88), ("small", 0.79)]


models = [
    {"name": "tiny", "score": 0.88},
    {"name": "base", "score": 0.91},
    {"name": "small", "score": 0.79},
    {"name": "zero", "score": 0.88},
]


def leaderboard(models: List[Dict]) -> List[Tuple[str, float]]:
    models_summary: List[Tuple[str, float]] = []
    models_summary = [(model["name"], model["score"]) for model in models]
    return sorted(models_summary, key = lambda k: (-k[1],k[0])) 


if __name__ == "__main__":
    print(leaderboard(models))
