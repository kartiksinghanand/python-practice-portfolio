from typing import List, Dict


# Day 7 - Problem 6
# Topic: Small product-style utility
#
# Task:
# Given a list of user actions, return:
# {
#   "total_actions": <int>,
#   "login_actions": <int>,
#   "logout_actions": <int>
# }
#
# Important:
# - count every record exactly once
# - only count "login" under login_actions
# - only count "logout" under logout_actions
#
# What to return:
# - total_actions = total number of records
# - login_actions = count of action == "login"
# - logout_actions = count of action == "logout"
#
# Expected output for current sample:
# {"total_actions": 4, "login_actions": 2, "logout_actions": 1}


actions = [
    {"user": "Aman", "action": "login"},
    {"user": "Diya", "action": "logout"},
    {"user": "Aman", "action": "login"},
    {"user": "Eshan", "action": "view"},
]


def action_summary(actions: List[Dict]) -> Dict[str, int]:
    users_actions : Dict[str, int] = {"total_actions":len(actions), "login_actions":0, "logout_actions": 0 }
    for action in actions:
        if action["action"] == "login" :
            users_actions["login_actions"] += 1
        elif action["action"] == "logout":
            users_actions["logout_actions"] += 1


    return users_actions

if __name__ == "__main__":
    print(action_summary(actions))
