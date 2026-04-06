from typing import List, Dict


# Day 6 - Problem 7
# Topic: Product-style summary
#
# Task:
# Given order records, return:
# {
#   "total_orders": <int>,
#   "delivered_orders": <int>,
#   "pending_orders": <int>
# }
#
# Important:
# - total_orders = count of all records
# - delivered_orders = status == "delivered"
# - pending_orders = status == "pending"


orders = [
    {"id": "O1", "status": "delivered"},
    {"id": "O2", "status": "pending"},
    {"id": "O3", "status": "delivered"},
    {"id": "O4", "status": "pending"},
    {"id": "O5", "status": "cancelled"},
]


def order_summary(orders: List[Dict]) -> Dict[str, int]:
    summary : Dict[str, int] = {}
    summary["total_orders"] = len(orders)
    for order in orders:
        if order["status"] not in summary and order["status"] is not "cancelled" :
            summary[order["status"]] = 1
        elif  order["status"] is not "cancelled":
            summary[order["status"]] += 1
    # print("summary: ",summary)
    summary["delivered_orders"] = summary.pop("delivered")
    summary["pending_orders"] = summary.pop("pending")
    return summary
            

if __name__ == "__main__":
    print(order_summary(orders))
