from typing import List, Dict


# Day 7 - Problem 1
# Topic: Nested aggregation
#
# Task:
# Given a list of orders, return a dictionary:
# customer -> total amount spent
#
# Important:
# - add all amounts for the same customer
# - return {} for empty input
#
# What to return:
# - one dictionary where each customer name maps to total spending
#
# Expected output for current sample:
# {"Aman": 200.0, "Diya": 300.0, "Eshan": 250.0}


orders = [
    {"customer": "Aman", "amount": 120.0},
    {"customer": "Diya", "amount": 300.0},
    {"customer": "Aman", "amount": 80.0},
    {"customer": "Eshan", "amount": 250.0},]
# orders = []


def customer_totals(orders: List[Dict]) -> Dict[str, float]:
    customer_spending :  Dict[str, float] = {}
    for order in orders:
        if order["customer"] not in customer_spending :
            customer_spending[order["customer"]] = order["amount"]
        else:
            customer_spending[order["customer"]] += order["amount"]

    return customer_spending
if __name__ == "__main__":
    print(customer_totals(orders))
