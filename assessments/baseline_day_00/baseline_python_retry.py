# Baseline Retry - Python
# File: baseline_python_retry.py
# Goal: reattempt baseline with guided hints (no full answers).
#
# Rules:
# 1) Solve from top to bottom.
# 2) Use hints only if blocked for >10 minutes.
# 3) Mark lookups with: # LOOKED_UP
# 4) Keep time <= 90 minutes.

from typing import List, Dict, Tuple

# Task 1 (Easy): List comprehension
# Given nums, create a new list of squares for even numbers only.
# Expected for sample: [4, 16, 36]
nums = [1, 2, 3, 4, 5, 6]

def even_squares(nums: List[int]) -> List[int]:
    # Hint 1: comprehension format -> [expr for item in iterable if condition]
    # Hint 2: even check -> x % 2 == 0
    return [x**2 for x in nums if x%2 == 0]


# Task 2 (Easy-Medium): Frequency map + sorting
# Return dict mapping each word to frequency.
# Then return list[tuple] sorted by:
# - frequency descending
# - word ascending (tie-break)
words = ["robot", "ai", "robot", "sensor", "ai", "ai","electricity"]

def word_stats(words: List[str]) -> Tuple[Dict[str, int], List[Tuple[str, int]]]:
    # Hint 1: build freq dict with a loop (or collections.Counter if you already know it).
    # Hint 2: sorted(..., key=lambda kv: (-kv[1], kv[0]))
    # Hint 3: return BOTH values exactly: freq_dict, sorted_items
    freq_dict = {}
    sorted_items = []
    items = set(words)
    for item in items:
        freq_dict[item] = words.count(item)
        x, y = item, words.count(item)
        sorted_items.append([x,y])
        
    
    sorted_items = sorted(sorted_items, key = lambda k: (-k[1], k[0]))
    # sorted_items=sorted_items[:]
    # sorted_items = sorted(sorted_items, key = lambda k: if k[])
    # for i in range(len(sorted_items)):
    #     tuple(sorted_items[i])
    x = [tuple(pint) for pint in sorted_items]
    sorted_items = x

    return freq_dict, sorted_items

        


        
# Task 3 (Medium): Class design (OOP basics)
# Create a RobotBattery class with:
# - capacity (int)
# - level (int)
# Methods:
# - drain(amount): reduce level but never below 0
# - charge(amount): increase level but never above capacity
# - is_low(): True if level < 20% of capacity

class RobotBattery:
    # Hint 1: constructor should accept exactly (capacity, level)
    # Hint 2: keep ONE source of truth for charge value (use self.level)
    # Hint 3: clamp with max/min
    def __init__(self, capacity: int, level: int):
        self.capacity = capacity
        self.level = level

    def drain(self, amount: int) -> None:
        self.level -= amount
        if self.level < 0:
            self.level = 0
        

    def charge(self, amount: int) -> None:
        self.level += amount
        if self.level > self.capacity:
            self.level = self.capacity

    def is_low(self) -> bool:
        if self.level < self.capacity*0.2:
            return True
        else:
            return False


# Task 4 (Medium): Debug + edge cases
# Implement first_non_repeating.
# Return None when no such element exists.

def first_non_repeating(numbers: List[int]):
    # Hint 1: two-pass approach:
    #   pass A: count frequencies
    #   pass B: first item with count 1
    # Hint 2: return None AFTER loop, not inside first mismatch branch.
    unique_nums = set(numbers)
    
    for num in numbers:
        if numbers.count(num) == 1:
            return num
        else:
            continue
    return None


# Task 5 (Medium): Small architecture thinking
# parse_sensor_packet(packet: str) -> Dict[str, float]
# Packet format: "temp=36.5;hum=45.2;dist=120.0"
# Return dict with float values.
# Ignore empty fields safely.

def parse_sensor_packet(packet: str) -> Dict[str, float]:
    # Hint 1: split packet by ';'
    # Hint 2: skip empty tokens after strip()
    # Hint 3: only parse token if '=' exists
    # Hint 4: split into key/value once -> split('=', 1)
    # Hint 5: convert value with float(...) inside try/except ValueError
    info = packet.split(";")
    sensors_dict = {}
    for item in info:
        if "=" in item:
            x = item.split("=")
            sensors_dict[x[0].strip()] = float(x[1].strip())
    return sensors_dict


if __name__ == "__main__":
    print("Task 1:", even_squares(nums))
    print("Task 2:", word_stats(words))

    b = RobotBattery(100, 30)
    b.drain(15)
    b.charge(5)
    print("Task 3:", b.level, b.is_low())

    print("Task 4:", first_non_repeating([2, 3, 2, 4, 3, 5, 4]))
    print("Task 5:", parse_sensor_packet("temp=36.5;hum=45.2;dist=120.0"))
    print("Task 5 (noisy):", parse_sensor_packet("temp=36.5;; hum=45.2;bad;dist=120.0;"))