from typing import List, Tuple


# Day 10 - Problem 3
# Topic: Sequence prep
#
# Task:
# Given a numeric series and window size, return a list of tuples:
# (window, next_value, delta)
#
# where:
# - window = list of consecutive values
# - next_value = value right after the window
# - delta = next_value - last value in the window
#
# If not enough values exist, return [].
#
# Expected output for current sample:
# [([10, 12], 15, 3), ([12, 15], 14, -1), ([15, 14], 20, 6)]


series = [10, 12, 15, 14, 20, 21, 15, 100]
window_size = 2


def make_delta_windows(series: List[int], window_size: int) -> List[Tuple[List[int], int, int]]:
    windows = []
    offset = 0

    for i in range(len(series)- window_size - 2):
        item = ((series[offset:window_size+i],series[window_size+i],series[window_size+i] - series[window_size + i - 1])) 
        windows.append(item)
        offset += 1

    return windows

        


if __name__ == "__main__":
    print(make_delta_windows(series, window_size))
