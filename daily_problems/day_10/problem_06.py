from typing import List


# Day 10 - Problem 6
# Topic: Medium-hard logic
#
# Task:
# Given a list of integers, return the length of the longest strictly increasing
# contiguous subarray.
#
# Example:
# [1, 2, 3, 2, 4, 5, 6] -> 4
# because [2, 4, 5, 6] has length 4.
#
# Important:
# - contiguous means elements must be next to each other
# - return 0 for empty input
#
# Expected output for current sample:
# 4


nums = [1, 2, 3, 2, 4, 5, 6, 1, 3,8,9,0]


def longest_increasing_contiguous(nums: List[int]) -> int:
    current_idx = 0
    next_idx = 1
    max_count = 0
    count = 0
    for i in range(len(nums)-1):
        if nums[current_idx] < nums[next_idx]:
            count += 1
            if max_count < count:
                max_count = count + 1
        elif nums[current_idx] >= nums[next_idx]:
            if max_count < count:
                max_count = count + 1
            count = 0
        current_idx += 1
        next_idx += 1
    return max_count
    


if __name__ == "__main__":
    print(longest_increasing_contiguous(nums))
