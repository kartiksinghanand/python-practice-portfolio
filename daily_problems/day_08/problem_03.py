from typing import List, Tuple


# Day 8 - Problem 3
# Topic: AI prep - sequence windows
#
# Task:
# Given a list of prices and a window size, create training windows.
#
# Example:
# prices = [10, 11, 12, 13], window_size = 2
# windows:
# [([10, 11], 12), ([11, 12], 13)]
#
# Important:
# - each item should be (input_window, target_value)
# - input_window must be a list
# - if not enough prices, return []
#
# What to return:
# - a list of tuples: (window_list, next_value)
#
# Expected output for current sample:
# [([100, 101, 102], 103), ([101, 102, 103], 104)]


prices = [100, 101, 102, 103, 104]
window_size = 3


def make_windows(prices: List[int], window_size: int) -> List[Tuple[List[int], int]]:
    windows = []
    for i in range(len(prices)):
        # if prices[window_size] == prices[-1]:
        #     break
        # else:
        window = (prices[i:i+window_size:],prices[window_size+i])
        windows.append(window)
        if window[1] == prices[-1]:
            break

    # windows = [(prices[i:window_size+i:1]) for i in range(0, len(windows))]

    # print("created windows: ", windows)
    return windows

if __name__ == "__main__":
    print(make_windows(prices, window_size))
