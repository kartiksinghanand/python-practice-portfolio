from typing import List, Dict


# Day 7 - Problem 3
# Topic: Validation + summary
#
# Task:
# Given a list of transaction strings like:
# "id=T1 amount=120 status=success"
#
# Return:
# {
#   "valid_transactions": <int>,
#   "success_transactions": <int>,
#   "total_amount": <float>
# }
#
# A valid transaction must contain:
# - id=...
# - amount=...
# - status=...
#
# Important:
# - ignore malformed or incomplete lines
# - total_amount = sum of amounts of valid transactions only
#
# What to return:
# - valid_transactions = count of valid lines only
# - success_transactions = among valid lines, count only status=success
# - total_amount = sum of amounts of valid lines only
#
# Expected output for current sample:
# {"valid_transactions": 3, "success_transactions": 2, "total_amount": 250.0}


transactions = [
    "id=T1 amount=120 status=success",
    "id=T2 amount=50 status=failed",
    "id=T3 status=success",
    "",
    "id=T4 amount=80 status=success",
]


def transaction_report(transactions: List[str]) -> Dict[str, float]:
    report: Dict[str, float] = {}
    total_amount = 0
    valid_transactions = []
    successful_transactions = []
    for transaction in transactions:
        if "id" in transaction and "amount" in transaction and "status" in transaction:
            valid_transactions.append(transaction)
    for txn in valid_transactions:
        if "status=success" in txn:
            successful_transactions.append(txn)
            # print("tokens",tokens)
        tokens = txn.split(" ")
        t,amt = tokens[1].split("=")
        total_amount += float(amt) 


    # print("Valid transactions: ", valid_transactions)

    report =  {
  "valid_transactions": len(valid_transactions),
  "success_transactions": len(successful_transactions),
  "total_amount": total_amount
    }   
    return report


if __name__ == "__main__":
    print(transaction_report(transactions))
