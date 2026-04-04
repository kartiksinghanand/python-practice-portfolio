# Day 2 - Problem 3 (Python Replacement)
# Topic: Product-style Python (clean functions + small data pipeline)
#
# Build a mini expense summary utility.
#
# Input:
# A list of dicts with keys: "category", "amount"
#
# Tasks:
# 1) total_spend(records): return total amount (float)
# 2) category_totals(records): return dict category -> total amount
# 3) top_category(records): return (category, amount) with highest spend
#    If records empty, return None
#
# Constraints:
# - Use clear function decomposition
# - Handle empty input safely
# - Keep output deterministic

from typing import List, Dict, Tuple, Optional

records = [
    {"category": "food", "amount": 250.0},
    {"category": "travel", "amount": 1200.0},
    {"category": "food", "amount": 150.0},
    {"category": "books", "amount": 500.0},
    {"category": "travel", "amount": 300.0},
]


def total_spend(records: List[Dict]) -> float:
    total_amount = [item["amount"] for item in records ]
    return sum(total_amount)
    


def category_totals(records: List[Dict]) -> Dict[str, float]:
    expenses : Dict[str,int] = {}
    
    for record in records:
        if record["category"] not in expenses:
            expenses[record["category"]] = record["amount"]
        else:
            expenses[record["category"]] += record["amount"]
    return expenses


def top_category(records: List[Dict]) -> Optional[Tuple[str, float]]:
    expenses = category_totals(records)
    top_spend = max(expenses, key= expenses.get)
    return (top_spend, expenses[top_spend])
     

if __name__ == "__main__":
    print("Total:", total_spend(records))
    print("Category totals:", category_totals(records))
    print("Top category:", top_category(records))