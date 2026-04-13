from typing import List, Dict


# Day 10 - Problem 10
# Topic: Harder practical logic
#
# Task:
# Given order events, return the first order id that becomes repeated.
# A repeated order id means the second time it appears in the list.
#
# Example:
# [{"id": "A"}, {"id": "B"}, {"id": "A"}] -> "A"
#
# Important:
# - return the first order id whose second appearance happens earliest
# - if no repeated id exists, return None
#
# Expected output for current sample:
# "A"


orders = [
    {"id": "A"},
    {"id": "B"},
    {"id": "C"},
    {"id": "A"},
    {"id": "B"},
]


def first_repeated_order(orders: List[Dict]) -> str | None:
    orders_list = []
    for order in orders:
        if order["id"] not in orders_list:
            orders_list.append(order["id"])
        else:
            return order["id"]


if __name__ == "__main__":
    print(first_repeated_order(orders))
