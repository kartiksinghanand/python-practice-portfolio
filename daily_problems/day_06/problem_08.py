from typing import List, Dict, Tuple


# Day 6 - Problem 8
# Topic: Aggregation + top item
#
# Task:
# Given sales records, return the product with the highest total sales amount
# as a tuple: (product_name, total_amount)
#
# Important:
# - first aggregate by product
# - then return the top product
# - if input is empty, return None


sales = [
    {"product": "pen", "amount": 100.0},
    {"product": "book", "amount": 300.0},
    {"product": "pen", "amount": 120.0},
    {"product": "bag", "amount": 250.0},
]


def top_product(sales: List[Dict]) -> Tuple[str, float] | None:
    product_sales = {}
    for sale in sales: 
        if sale["product"] not in product_sales:
            product_sales[sale["product"]] = sale["amount"]
        else:
            product_sales[sale["product"]] += sale["amount"]
    sorted_products  = sorted(product_sales, key = product_sales.get)
    return (sorted_products[-1],product_sales[sorted_products[-1]])

if __name__ == "__main__":
    print(top_product(sales))
