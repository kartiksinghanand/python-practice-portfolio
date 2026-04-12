from typing import List


# Day 8 - Problem 2
# Topic: Data cleaning
#
# Task:
# Given a price series, return a cleaned list of floats.
#
# Rules:
# - ignore None
# - ignore invalid strings like "bad"
# - convert valid numeric strings to float
# - keep original order
#
# What to return:
# - a cleaned list of float values only
#
# Expected output for current sample:
# [100.0, 101.5, 99.0, 103.25]


prices = [100, "101.5", None, "bad", 99, "103.25"]


def clean_prices(prices: List[object]) -> List[float]:
    cleaned_prices = []
    for price in prices:
        if type(price) == type(5):
            cleaned_prices.append(float(price))
        elif type(price) == type("sassy"):
            try:
                cleaned_prices.append(float(price))
            except:
                continue                    
        else:
            continue
    # print("Cleaned prices: ", clean_prices)
    return cleaned_prices

if __name__ == "__main__":
    print(clean_prices(prices))
