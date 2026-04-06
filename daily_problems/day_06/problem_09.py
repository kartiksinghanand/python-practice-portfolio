from typing import List, Dict


# Day 6 - Problem 9
# Topic: Nested parsing + reporting
#
# Each record looks like:
# "team=A status=win"
#
# Task:
# Write team_report(records) that returns:
# {
#   "total_matches": <int>,
#   "wins": {"A": 2, "B": 1, ...}
# }
#
# Important:
# - only count valid lines containing both team and status
# - only include records with status=win in the wins dictionary


records = [
    "team=A status=win",
    "team=B status=loss",
    "team=A status=win",
    "team=C status=win",
    "",
]


def team_report(records: List[str]) -> Dict[str, object]:
    ignorables = 0
    total_matches = len(records)
    report : Dict[str, object] = {}
    win_list ={}
    for record in records:
        if len(record) == 0 or "loss" in record:
            ignorables += 1
        else :
            continue
    report["total_matches"] = total_matches - ignorables
    print("report: ",report)
    for record in records:
        if "win" in record:
            tokens = record.split(" ")
            team, team_name = tokens[0].split("=")
            if team_name not in win_list:
                win_list[team_name] = 1
            else:
                win_list[team_name] += 1
        else:
            continue
    report["wins"] = win_list
    return report


if __name__ == "__main__":
    print(team_report(records))
