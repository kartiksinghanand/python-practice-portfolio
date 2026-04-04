# Baseline Test - Python
# File: baseline_python.py
# Goal: evaluate your current Python level (syntax, logic, functions, OOP, comprehension)
#
# Instructions:
# 1) Solve all tasks in this file.
# 2) Do not use AI help while solving.
# 3) Keep total time <= 90 minutes.
# 4) Add comments where you are unsure.

from dataclasses import dataclass
from typing import List, Dict

# Task 1 (Easy): List comprehension
# Given nums, create a new list of squares for even numbers only.
# Expected for sample: [4, 16, 36]
nums = [1, 2, 3, 4, 5, 6]

def even_squares(nums: List[int]) -> List[int]:
    squares = [x**2 for x in nums if x % 2 == 0]
    return squares


# Task 2 (Easy-Medium): Frequency map + sorting
# Return dict mapping each word to frequency.
# Then return a list of tuples sorted by:
# - frequency descending
# - word ascending (tie-break)
words = ["robot", "ai", "robot", "sensor", "ai", "ai"]

def word_stats(words: List[str]):
    unique_words = set(words)
    unique_words = sorted(unique_words)
    freq_dict = {}
    for name in unique_words:
        freq_dict[name] = words.count()
        sorted_items = ()
        sorted_items = tuple(sorted(freq_dict.items()))

    # return freq_dict, sorted_items
    


# Task 3 (Medium): Class design (OOP basics)
# Create a RobotBattery class with:
# - capacity (int)
# - level (int)
# Methods:
# - drain(amount): reduce level but never below 0
# - charge(amount): increase level but never above capacity
# - is_low(): True if level < 20% of capacity

class RobotBattery:
    def __init__ (self, capacity, level, amount):
        self.capacity = capacity
        self.level = level
        self.amount = amount

    def drain(self, amount: int):        
        self.amount = self.amount - amount
        if self.amount < 0:
            self.amount = 0
        
    def charge (self, amount):
        self.amount = self.amount + amount 
        if self.amount > 100:
            self.amount = 100
    
    def is_low(self):
        if self.amount < 20:
            return True


# Task 4 (Medium): Debug + edge cases
# Implement first_non_repeating from your Day 1 problem.
# Return None when no such element exists.

numbers = [4, 5, 1, 2, 0, 4, 1, 2, 5, 9, 0, 7, 9]

def first_non_repeating(numbers: List[int]):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
        else:
            return None
    


# Task 5 (Medium): Small architecture thinking
# Write a function parse_sensor_packet(packet: str) -> Dict[str, float]
# Packet format: "temp=36.5;hum=45.2;dist=120.0"
# Return dict with float values.
# Ignore empty fields safely.

def parse_sensor_packet(packet: str) -> Dict[str, float]:
    sensors = packet.split(";")
    sensors_stats = {}
    for sensor in sensors:
        sensor_info = sensor.split("=")
        sensors_stats[sensor_info[0]] = sensor_info[1]    
    return sensors_stats

if __name__ == "__main__":
    print("Task 1:", even_squares(nums))
    print("Task 2:", word_stats(words))

    b = RobotBattery(100, 30)
    b.drain(15)
    b.charge(5)
    print("Task 3:", b.level, b.is_low())

    print("Task 4:", first_non_repeating([2, 3, 2, 4, 3, 5, 4]))
    print("Task 5:", parse_sensor_packet("temp=36.5;hum=45.2;dist=120.0"))