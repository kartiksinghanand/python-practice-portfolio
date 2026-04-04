from typing import List, Tuple


# Day 8 - Problem 7
# Topic: Data split
#
# Task:
# Given a dataset list and a split index, return:
# (train_data, validation_data)
#
# Rules:
# - train_data = items before split index
# - validation_data = items from split index onward
# - do not modify original order
#
# What to return:
# - a tuple of two lists
#
# Expected output for current sample:
# ([1, 2, 3], [4, 5, 6])


data = [1, 2, 3, 4, 5, 6]
split_index = 3


def train_val_split(data: List[int], split_index: int) -> Tuple[List[int], List[int]]:
    # TODO
    pass


if __name__ == "__main__":
    print(train_val_split(data, split_index))
