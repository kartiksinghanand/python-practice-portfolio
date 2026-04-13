from typing import List, Dict


# Day 10 - Problem 1
# Topic: Practical aggregation
#
# Task:
# Given transaction records, return a dictionary:
# user -> total amount spent
#
# Important:
# - add all amounts for the same user
# - return {} for empty input
#
# Expected output for current sample:
# {"Aman": 170.0, "Diya": 120.0, "Eshan": 90.0}


transactions = [
    {"user": "Aman", "amount": 100.0},
    {"user": "Diya", "amount": 120.0},
    {"user": "Aman", "amount": 70.0},
    {"user": "Eshan", "amount": 90.0},
]


def user_totals(transactions: List[Dict]) -> Dict[str, float]:
    transaction_summary :  Dict[str, float] = {}
    for transaction in transactions:
        if transaction["user"] in transaction_summary:
            transaction_summary[transaction["user"]] += transaction["amount"]
        else:
            transaction_summary[transaction["user"]] = transaction["amount"]
    return transaction_summary

if __name__ == "__main__":
    print(user_totals(transactions))
