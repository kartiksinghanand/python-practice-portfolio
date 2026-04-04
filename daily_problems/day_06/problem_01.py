from typing import List, Dict


# Day 6 - Problem 1
# Topic: Aggregation
#
# Task:
# Given a list of expense records, return a dictionary:
# category -> total amount
#
# Important:
# - add all amounts in the same category
# - return {} for empty input


expenses = [
    {"category": "food", "amount": 120.0},
    {"category": "travel", "amount": 500.0},
    {"category": "food", "amount": 80.0},
    {"category": "books", "amount": 300.0},
]


def expense_totals(expenses: List[Dict]) -> Dict[str, float]:
    total_expense : Dict[str, float] = {}
    for expenditure in expenses:
        if expenditure["category"] not in total_expense:
            total_expense[expenditure["category"]] = expenditure["amount"]
        else:
            total_expense[expenditure["category"]] += expenditure["amount"]
    return total_expense
    


if __name__ == "__main__":
    print(expense_totals(expenses))
