from typing import List, Dict, Tuple


# Day 5 - Problem 8
# Topic: Sorting + tie-break
#
# Task:
# Given a list of player scores, return the leaderboard as a list of tuples:
# (name, score), sorted by:
# - score descending
# - name ascending
#
# Important:
# - return tuples, not dictionaries
# - if two players have the same score, sort them alphabetically by name


players = [
    {"name": "Aman", "score": 88},
    {"name": "Bina", "score": 95},
    {"name": "Chirag", "score": 88},
    {"name": "Diya", "score": 72},
]


def leaderboard(players: List[Dict]) -> List[Tuple[str, int]]:
    info = []
    for player in players:
        info.append((player["name"],player["score"]))

    # print("info: ", info)

    sorted_players = sorted(info, key = lambda k: (-k[1],k[0]))
    # information = [x[0] for x in sorted_players]
    return sorted_players
if __name__ == "__main__":
    print(leaderboard(players))
