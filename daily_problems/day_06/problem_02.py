from typing import List


# Day 6 - Problem 2
# Topic: Filtering
#
# Task:
# Given a list of integers, return only the numbers that are divisible by 3 or 5.
#
# Important:
# - keep input order
# - return [] if no numbers match


nums = [2, 3, 5, 7, 10, 12, 14, 15]


def divisible_by_3_or_5(nums: List[int]) -> List[int]:
    answers = []
    for num in nums:
        if num % 3 == 0 or num % 5==0:
            answers.append(num)
    return answers


if __name__ == "__main__":
    print(divisible_by_3_or_5(nums))
