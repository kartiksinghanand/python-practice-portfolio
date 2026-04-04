from typing import List


# Day 5 - Problem 5
# Topic: List transformation
#
# Task:
# Given a list of integers, return a new list where:
# - even numbers are squared
# - odd numbers are cubed
#
# Keep the same order as the input list.
#
# Example:
# [2, 3, 4] -> [4, 27, 16]


nums = [2, 3, 4, 5, 6]


def transform_numbers(nums: List[int]) -> List[int]:
    squares_and_cubes = []
    for num in nums:
        if num%2 ==0:
            squares_and_cubes.append(num**2)
        else:
            squares_and_cubes.append(num**3)
    return squares_and_cubes


if __name__ == "__main__":
    print(transform_numbers(nums))
