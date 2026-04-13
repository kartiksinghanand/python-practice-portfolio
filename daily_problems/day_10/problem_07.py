from typing import List


# Day 10 - Problem 7
# Topic: Medium-hard string logic
#
# Task:
# Given a string, return the length of the longest substring without repeating characters.
#
# Examples:
# "abcabcbb" -> 3
# "bbbbb" -> 1
# "pwwkew" -> 3
#
# Important:
# - substring means contiguous
# - return 0 for empty string
#
# Expected output for current sample:
# 3


# s = "pwwkew"
s = "dvdf"

def longest_unique_substring_length(s: str) -> int:
    string_list = []
    substring = ""
    for ch in s:

        if ch not in substring:    # s = "pwwkew"
            substring += ch
        elif ch in substring:
            string_list.append(substring)
            substring = substring[substring.index(ch)+1:] 
            substring += ch
        if ch == s[-1]:
            string_list.append(substring)
    



    max_string = max(string_list, key = lambda k : len(k))
    return len(max_string)

if __name__ == "__main__":
    print(longest_unique_substring_length(s))
