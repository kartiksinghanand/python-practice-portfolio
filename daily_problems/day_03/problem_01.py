from typing import List, Dict


# Day 3 - Problem 1
# Topic: Dict + list fluency
#
# Task:
# Given a list of words, return a dictionary where:
# - key = word
# - value = list of positions where that word appears
#
# Example:
# ["ai", "robot", "ai", "ml"] -> {"ai": [0, 2], "robot": [1], "ml": [3]}
#
# Requirements:
# 1) Preserve index positions correctly
# 2) Return an empty dict for empty input


def word_positions(words: List[str]) -> Dict[str, List[int]]:
    word_position : Dict[str, List[int]] = {}
    enumerated_list = list(enumerate(words))
    for pair in enumerated_list:
        if pair[1] not in word_position:
            word_position[pair[1]] = [x[0] for x in enumerated_list if x[1] == pair[1] ]
        else:
            continue

    return word_position

if __name__ == "__main__":
    tests = [
        ["ai", "robot", "ai", "ml"],
        ["sensor", "sensor", "sensor"],
        [],
    ]

    for t in tests:
        print(t, "->", word_positions(t))
