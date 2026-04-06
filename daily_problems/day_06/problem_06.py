from typing import List


# Day 6 - Problem 6
# Topic: String cleanup
#
# Task:
# Given a list of names, return a cleaned list where:
# - surrounding spaces are removed
# - empty names are ignored
# - all remaining names are converted to title case
#
# Example:
# ["  aman ", "", "diya"] -> ["Aman", "Diya"]


names = ["  aman ", "", "diya", "  ESHAN", "   "]


def clean_names(names: List[str]) -> List[str]:
    tokens = []
    for token in names:
        token = token.strip()
        if len(token) != 0:
            tokens.append(token.title()) 

    return tokens



if __name__ == "__main__":
    print(clean_names(names))
