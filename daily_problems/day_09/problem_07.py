from typing import List, Dict


# Day 9 - Problem 7
# Topic: Log parsing
#
# Each line looks like:
# "user=alice action=click page=home"
#
# Task:
# Return a dictionary:
# action -> count
#
# Important:
# - count only valid action fields
# - ignore malformed parts safely
# - count every valid line independently
#
# Expected output for current sample:
# {"click": 2, "view": 1}


logs = [
    "user=alice action=click page=home",
    "user=bob action=view page=pricing",
    "user=alice action=click page=pricing",
    "badpart user=carol",
]


def action_counts(logs: List[str]) -> Dict[str, int]:
    click = 0
    view = 0
    for log in logs:
        if "action" in log and "user" in log and "page" in log:
            tokens = log.split(" ")
            i = 0
            for token in tokens:
                if "action" in token:
                    i = tokens.index(token)
                else:
                    continue
            action, act = tokens[i].split("=")
            
            if act == "click":
                click += 1 
            elif act == "view":
                view += 1
    return {"click": click, "view": view}


if __name__ == "__main__":
    print(action_counts(logs))
