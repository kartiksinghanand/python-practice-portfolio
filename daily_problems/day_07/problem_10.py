from typing import List, Dict

# Day 7 - Problem 10
# Topic: Portfolio / proof task
#
# Task:
# Create a function build_day_report(results) that takes a list like:
# [
#   {"problem": 1, "status": "done"},
#   {"problem": 2, "status": "done"},
#   {"problem": 3, "status": "pending"}
# ]
#
# Return:
# {
#   "completed": <int>,
#   "pending": <int>,
#   "completion_rate": <float>
# }
#
# Important:
# - completion_rate = completed / total_items
# - if input is empty, completion_rate should be 0.0
#
# What to return:
# - completed = number of items with status == "done"
# - pending = number of items with status != "done"
# - completion_rate = completed / total_items
#
# Expected output for current sample:
# {"completed": 3, "pending": 1, "completion_rate": 0.75}


results = [
    {"problem": 1, "status": "done"},
    {"problem": 2, "status": "done"},
    {"problem": 3, "status": "pending"},
    {"problem": 4, "status": "done"},
]


def build_day_report(results: List[Dict]) -> Dict[str, float]:
    # report : Dict[str, float] = {}
    completed = 0
    pending = 0
    for result in results:
        if result["status"] == "done":
            completed += 1
        elif result["status"] == "pending":
            pending += 1
    completion_rate = completed / (len(results))
    return {"completed": completed, "pending": pending, "completion_rate" : completion_rate}
if __name__ == "__main__":
    print(build_day_report(results))
