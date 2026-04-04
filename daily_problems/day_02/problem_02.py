# Day 2 - Problem 2 (Python)
# Topic: Lambda + List Comprehension + Sorting rules
#
# Task A:
# Given transactions below, create a list of HIGH value transaction ids
# where amount >= 500.
# Use list comprehension only.
# Expected ids for sample: ["T2", "T4", "T5"]
#
# Task B:
# Build merchant frequency dict from transactions.
#
# Task C:
# Create sorted_merchants as list of tuples (merchant, freq)
# sorted by:
# - freq descending
# - merchant ascending (tie-break)
# Use sorted + lambda key.

from typing import List, Dict, Tuple

transactions = [
    {"id": "T1", "merchant": "alpha", "amount": 120},
    {"id": "T2", "merchant": "beta", "amount": 900},
    {"id": "T3", "merchant": "alpha", "amount": 450},
    {"id": "T4", "merchant": "delta", "amount": 700},
    {"id": "T5", "merchant": "beta", "amount": 500},
    {"id": "T6", "merchant": "alpha", "amount": 300},
]


def analyze_transactions(transactions: List[Dict]) -> Tuple[List[str], Dict[str, int], List[Tuple[str, int]]]:
    # Task A
    high_value_ids = [item['id'] for item in transactions if item['amount'] >=500 ]

    # Task B
    merchant_freq: Dict[str, int] = {}
    # merchant_freq = [item.get("merchant") for item in transactions] 
    # merchant_freq = merchant_freq
    # x = [{item: merchant_freq.count(item)} for item in merchant_freq]
    # for item in x:
    #     if x.count(item) > 1:
    #         x.remove(item)
    # merchant_freq = x
    for item in transactions:
        if item["merchant"] in merchant_freq:
            merchant_freq[item["merchant"]] += 1
        else:
            merchant_freq[item["merchant"]] = 1
    
    # Task C
    sorted_merchants: List[Tuple[str, int]] = []
    # for item in merchant_freq:
    # for item in merchant_freq:
    # sorted_merchants = [tuple() for entry in merchant_freq]
    # sorted_merchants = [item for item in merchant_freq]
    merchant_names = list(merchant_freq.keys())
    # sorted_merchants = [tuple(name) for name in merchant_names ]
    print("Merchant names: ", merchant_names)
    x = list(merchant_freq.items())
    print("x --->",x)
    sorted_merchants = sorted(merchant_freq.items(), key = lambda k : (-k[1],k[0])) 

    return high_value_ids, merchant_freq, sorted_merchants


if __name__ == "__main__":
    ids, freq, sorted_m = analyze_transactions(transactions)
    print("High value ids:", ids)
    print("Merchant freq:", freq)
    print("Sorted merchants:", sorted_m)