from typing import List, Tuple


# Day 6 - Problem 5
# Topic: Sorting
#
# Task:
# Given a list of tuples (task_name, priority), return them sorted by:
# - priority descending
# - task_name ascending


tasks = [
    ("email", 2),
    ("deploy", 5),
    ("backup", 2),
    ("report", 4),
]


def sort_tasks(tasks: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    sorted_tasks = sorted(tasks, key = lambda k: (-k[1],k[0])) 
    return sorted_tasks


if __name__ == "__main__":
    print(sort_tasks(tasks))
