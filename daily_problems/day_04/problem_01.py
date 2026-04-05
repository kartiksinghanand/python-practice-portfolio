from typing import List, Dict


# Day 4 - Problem 1
# Topic: Aggregation with dictionaries
#
# Task:
# Given a list of sales records, return a dictionary:
# product -> total quantity sold
#
# Example:
# [{"product": "pen", "qty": 2}, {"product": "pen", "qty": 3}]
# ->
# {"pen": 5}


records = [
    {"product": "pen", "qty": 2},
    {"product": "book", "qty": 1},
    {"product": "pen", "qty": 3},
    {"product": "bag", "qty": 2},
    {"product": "book", "qty": 4},
]


def product_totals(records: List[Dict]) -> Dict[str, int]:
    item: Dict[str, int] = {}
    for each_record in records:
        if each_record["product"] in item:
            item[each_record["product"]] += each_record["qty"]
        else:
            item[each_record["product"]] = each_record["qty"]
    # print("Items: ",item)
    return item

if __name__ == "__main__":
    print(product_totals(records))
