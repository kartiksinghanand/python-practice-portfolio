from typing import List, Dict


# Day 9 - Problem 10
# Topic: Mini product-style summary
#
# Task:
# Given trade records, return:
# {
#   "buy_count": <int>,
#   "sell_count": <int>,
#   "net_quantity": <int>
# }
#
# Rules:
# - buy_count = number of records with side == "buy"
# - sell_count = number of records with side == "sell"
# - net_quantity = sum(buy quantities) - sum(sell quantities)
#
# Expected output for current sample:
# {"buy_count": 2, "sell_count": 2, "net_quantity": 4}


trades = [
    {"side": "buy", "qty": 10},
    {"side": "sell", "qty": 3},
    {"side": "buy", "qty": 5},
    {"side": "sell", "qty": 8},
]


def trade_summary(trades: List[Dict]) -> Dict[str, int]:
    buy = 0
    sell = 0
    for trade in trades:
        if trade["side"] == "buy":
            buy += 1
        else:
            sell += 1
    return  {
  "buy_count": buy,
  "sell_count": sell,
  "net_quantity": buy + sell
    }




if __name__ == "__main__":
    print(trade_summary(trades))
