from typing import List, Dict


# Day 5 - Problem 7
# Topic: Dictionary filtering
#
# Task:
# Given a list of products, return names of products whose price is <= budget.
# Return names sorted by price ascending.
#
# Important:
# - if two products have the same price, keep their relative order from the input
# - return only product names, not full dictionaries
#
# Example:
# budget=500
# ["pen", "notebook", ...]


products = [
    {"name": "pen", "price": 20},
    {"name": "bottle", "price": 10},
    
    {"name": "notebook", "price": 120},
    {"name": "bag", "price": 900},
    {"name": "mouse", "price": 450},
    {"name": "keyboard", "price": 700},
]

budget = 500


def affordable_products(products: List[Dict], budget: int) -> List[str]:
    products_list = []
    for product in products:
        if product["price"] <= budget:
            products_list.append((product["name"],product["price"]))
    # print("products_list", products_list)
    products_list_sorted = sorted(products_list, key = lambda k: k[-1])
    products_list = [prod[0] for prod in products_list_sorted]
    return products_list
if __name__ == "__main__":
    print(affordable_products(products, budget))
