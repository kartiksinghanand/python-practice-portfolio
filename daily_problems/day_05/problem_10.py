from typing import List, Dict


# Day 5 - Problem 10
# Topic: Product-style mini task
#
# Task:
# Given transaction records, return a summary:
# {
#   "total_amount": <float>,
#   "successful_count": <int>,
#   "failed_count": <int>
# }
#
# A record is successful if status == "success".
#
# Important:
# - total_amount = sum of amounts of all transactions, not only successful ones
# - successful_count = number of records with status == "success"
# - failed_count = number of records with status != "success"


transactions = [
    {"id": "T1", "amount": 120.0, "status": "success"},
    {"id": "T2", "amount": 90.0, "status": "failed"},
    {"id": "T3", "amount": 300.0, "status": "success"},
    {"id": "T4", "amount": 50.0, "status": "failed"},
]


def transaction_summary(transactions: List[Dict]) -> Dict[str, float]:
    summary = {"total_amount": 0,"successful_count" : 0, "failed_count": 0}
    for transaction in transactions:
        summary["total_amount"]  += transaction["amount"]
        if transaction["status"] == "success":
            summary["successful_count"] += 1
        elif transaction["status"] == "failed":
            summary["failed_count"] += 1  
    return summary

if __name__ == "__main__":
    print(transaction_summary(transactions))
