from typing import List, Dict


# Day 6 - Problem 10
# Topic: Product-style mini task
#
# Task:
# Given support tickets, return a summary:
# {
#   "high_priority": <int>,
#   "low_priority": <int>,
#   "open_tickets": <int>
# }
#
# Important:
# - high_priority = priority == "high"
# - low_priority = priority == "low"
# - open_tickets = status == "open"
# - count each ticket independently


tickets = [
    {"id": "T1", "priority": "high", "status": "open"},
    {"id": "T2", "priority": "low", "status": "closed"},
    {"id": "T3", "priority": "high", "status": "open"},
    {"id": "T4", "priority": "low", "status": "open"},
]


def ticket_summary(tickets: List[Dict]) -> Dict[str, int]:
    high_priority = 0
    low_priority = 0
    open_tickets = 0
    for ticket in tickets:
       if ticket["priority"] == "high":
           high_priority += 1
       elif ticket["priority"] == "low":
           low_priority += 1  
       if ticket["status"] == "open":
           open_tickets += 1
       else:
           continue
    return {
  "high_priority": high_priority,
  "low_priority": low_priority,
  "open_tickets": open_tickets
}

if __name__ == "__main__":
    print(ticket_summary(tickets))
