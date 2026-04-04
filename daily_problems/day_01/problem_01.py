# Day 1 - Problem 1 (Python)
# Task:
# Given the list below, return the first non-repeating element.
# Constraints: O(n) time, O(n) space.
#
# Input list:
# nums = [4, 5, 1, 2, 0, 4, 1, 2, 5, 9, 0, 7, 9]
#
# Expected idea:
# - Count frequencies
# - Scan left to right and return first value with frequency 1
#
# If no non-repeating element exists, return None.

nums = [4, 5, 1, 2, 0, 4, 1, 2, 5, 9, 0, 7, 9]


def first_non_repeating(nums):
    values = set(nums)
    


if __name__ == "__main__":
    result = first_non_repeating(nums)
    print("First non-repeating element:", result)