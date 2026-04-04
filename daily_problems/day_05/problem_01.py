from typing import List, Dict


# Day 5 - Problem 1
# Topic: Grouping and aggregation
#
# Task:
# Given a list of task records, return a dictionary:
# status -> count of tasks with that status
# Count every task in the input exactly once.
# Do not sort the result.
#
# Example:
# [{"status": "open"}, {"status": "done"}, {"status": "open"}]
# ->
# {"open": 2, "done": 1}


tasks = [
    {"id": 1, "status": "open"},
    {"id": 2, "status": "done"},
    {"id": 3, "status": "open"},
    {"id": 4, "status": "in_progress"},
    {"id": 5, "status": "done"},
]


def status_counts(tasks: List[Dict]) -> Dict[str, int]:
    status : Dict[str, int] = {}
    for task in tasks:
        if task["status"] not in status:
            status[task["status"]] = 1
        else:
            status[task["status"]] += 1 
    return status

if __name__ == "__main__":
    print(status_counts(tasks))
