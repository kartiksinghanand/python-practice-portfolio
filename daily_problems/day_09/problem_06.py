from typing import List


# Day 9 - Problem 6
# Topic: OOP intro 2
#
# Task:
# Create a class Counter with methods:
# - increment()
# - decrement()
# - value()
# - reset()
#
# Important:
# - initial value should be 0
# - increment() should increase the current value by 1
# - decrement() should decrease the current value by 1
# - value() should return the current integer value
# - reset should bring it back to 0
# - store the running count inside the object
#
# What to do:
# - implement the class so the object remembers its current count
# - each method should update or return that same stored value
#
# Expected behavior for current sample:
# after increment, increment, decrement -> value is 1
# after reset -> value is 0
#
# Expected printed output for current sample:
# 1
# 0


class Counter:
    def __init__ (self): 
        self._value : int = 0

    def increment(self):
        self._value += 1 

    def decrement(self):
        self._value -= 1 


    def value(self):
        return self._value

    def reset(self):
        self._value = 0


if __name__ == "__main__":
    c = Counter()
    c.increment()
    c.increment()
    c.decrement()
    print(c.value())
    c.reset()
    print(c.value())
