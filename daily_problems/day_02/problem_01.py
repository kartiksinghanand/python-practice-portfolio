# Day 2 - Problem 1 (Python)
# Topic: Time complexity improvement (O(n) target)
#
# Task:
# Implement first_non_repeating_optimized(nums) in O(n) time.
#
# Requirements:
# 1) Do NOT use nums.count(...) inside loop.
# 2) Use 2-pass frequency approach.
# 3) Return None if no non-repeating element exists.
#
# Test cases:
# [2, 3, 2, 4, 3, 5, 4] -> 5
# [1, 1, 2, 2] -> None
# [7] -> 7

from typing import List, Optional


def first_non_repeating_optimized(nums: List[int]) -> Optional[int]:
    # number_set = set(nums)
    # freq = [(item, nums.count(item)) for item in nums]
    # freq = []
    # print(freq)
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    # print(freq)
    for item in nums:
        if freq[item] == 1:
            return item
    
    return None
    # # non_repeating_element = [item[0] for item in freq if item[1] == 1]
    # if len(non_repeating_element)>0:
    #     return non_repeating_element[0]
    # else:
    #     return None
if __name__ == "__main__":
    tests = [
        [2, 3, 2, 4, 3, 5, 4],
        [1, 1, 2, 2],
        [7],
    ]

    for t in tests:
        print(t, "->", first_non_repeating_optimized(t))
    # print(first_non_repeating_optimized([1,2,3,4,1,2,5]))    