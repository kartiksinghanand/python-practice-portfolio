from typing import List


# Day 8 - Problem 6
# Topic: OOP intro
#
# Task:
# Create a class RunningAverage with methods:
# - add(value): add one number
# - value(): return current average as float
# - reset(): clear stored values
#
# Important:
# - if no values are stored, value() should return 0.0
#
# Expected behavior for current sample:
# after adding 10, 20, 30 -> average is 20.0
# after reset -> average is 0.0


class RunningAverage:
    def __init__(self):
        self.core_values = []
    def add(self, value):
        (self.core_values).append(value)
        # print("Values: ",self.core_values)
    def value(self):
        if len(self.core_values) == 0:
            return 0.0
        else:
            return sum(self.core_values)/len(self.core_values)
    def reset(self):
        self.core_values = []


if __name__ == "__main__":
    avg = RunningAverage()
    avg.add(10)
    avg.add(20)
    avg.add(30)
    print(avg.value())
    avg.reset()
    print(avg.value())
