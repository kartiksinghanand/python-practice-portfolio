from typing import List


# Day 5 - Problem 4
# Topic: String processing
#
# Task:
# Given a list of words, return a new list containing only palindrome words.
# Keep original order.
#
# A palindrome reads the same forward and backward.
# Example: "level", "madam", "radar"
#
# Example:
# ["level", "robot", "madam"] -> ["level", "madam"]


words = ["level", "robot", "madam", "python", "radar", "code"]


def palindromes(words: List[str]) -> List[str]:
    palindrome_words = []
    for word in words:
        if word == word[-1::-1]:
            # print("Palindrome words: ", word)
            palindrome_words.append(word)
    return palindrome_words

if __name__ == "__main__":
    print(palindromes(words))
