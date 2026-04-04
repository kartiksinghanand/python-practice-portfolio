from typing import List, Dict


# Day 5 - Problem 6
# Topic: Frequency counting
#
# Task:
# Given a sentence, count frequency of each word.
# Ignore case.
#
# Important:
# - convert the whole sentence to lowercase first
# - split words by spaces
# - return a dictionary word -> count
#
# Example:
# "AI ai Robot" -> {"ai": 2, "robot": 1}


sentence = "AI ai Robot robot ai code"


def word_frequency(sentence: str) -> Dict[str, int]:
    words = sentence.split(" ")
    freq : Dict[str, int] = {}
    for word in words:
        if word.lower() not in freq:
            freq[word.lower()] = 1
        else:
            freq[word.lower()] += 1
    return freq

if __name__ == "__main__":
    print(word_frequency(sentence))
