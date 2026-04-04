from typing import List, Dict


# Day 4 - Problem 3
# Topic: Parsing + summary report
#
# Each event string looks like:
# "type=click user=alice page=home"
#
# Task:
# Write event_summary(events) that returns:
# {
#   "total_events": <int>,
#   "by_type": {"click": 2, "view": 1, ...}
# }
#
# Requirements:
# - Ignore malformed parts safely
# - Ignore empty lines
# - Return {"total_events": 0, "by_type": {}} for empty input


events = [
    "type=click user=alice page=home",
    "type=view user=bob page=pricing",
    "type=click user=alice page=pricing",
    "",
    "badpart user=carol",
]


def event_summary(events: List[str]) -> Dict[str, object]:
    summary: Dict[str, object] = {}
    ignorables = 0
    for each_event in events:
        if len(each_event) == 0 or "badpart" in each_event:
            ignorables +=1
    print("ignorables: ",ignorables)
    summary["total_events"] = len(events) - ignorables  
    by_type = {}
    for each_event in events:
        event = each_event.split(" ")
        if "type" in event[0]:
            x = event[0].split("=")
            if x[1] not in by_type:
                by_type[x[1]] = 1
            else:
                by_type[x[1]] +=1
        else:
            continue
        summary["by_type"] = by_type
    return summary
if __name__ == "__main__":
    print(event_summary(events))
