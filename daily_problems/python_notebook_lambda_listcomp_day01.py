"""
Python Notebook - Lambda + List Comprehension (Day 1)
Instructions:
1) Is file ko top to bottom run karo.
2) Jahan TODO hai, khud solve karo.
3) End me outputs verify karo.
"""

# -----------------------------
# Section A: Lambda Basics
# -----------------------------

# Lambda syntax:
# lambda arguments: expression

square = lambda x: x * x
print("A1 square(5):", square(5))  # 25

add = lambda a, b: a + b
print("A2 add(3, 7):", add(3, 7))  # 10

# Lambda with sorted
nums = [5, 1, 9, 2]
print("A3 sorted ascending:", sorted(nums, key=lambda x: x))
print("A4 sorted descending:", sorted(nums, key=lambda x: -x))

pairs = [("ai", 3), ("robot", 2), ("sensor", 1), ("ml", 3)]
print("A5 sort by count desc, word asc:", sorted(pairs, key=lambda kv: (-kv[1], kv[0])))


# -----------------------------
# Section B: List Comprehension Basics
# -----------------------------

# Syntax:
# [expression for item in iterable if condition]

values = [1, 2, 3, 4, 5, 6]

squares = [x * x for x in values]
print("B1 squares:", squares)

even_squares = [x * x for x in values if x % 2 == 0]
print("B2 even squares:", even_squares)

words = ["ai", "robot", "ml"]
upper_words = [w.upper() for w in words]
print("B3 uppercase:", upper_words)

length_map = [(w, len(w)) for w in words]
print("B4 word lengths:", length_map)


# -----------------------------
# Section C: Practice TODOs
# -----------------------------

# Q1: Lambda use karke number ko double karo.
# Expected: 18 when input is 9
# TODO:
double = lambda x: 2*x
# print("Q1:", double(9))

# Q2: sorted + lambda se [5, 1, 9, 2] ko descending sort karo.
# Expected: [9, 5, 2, 1]
# TODO:

q2 = sorted(nums, key=lambda x: -x) 
# print("Q2:", q2)

# Q3: List comprehension se 1..10 me se odd numbers nikalo.
# Expected: [1, 3, 5, 7, 9]
# 
q3 = [i for i in range(1,11) if i % 2 not == 0]
# print("Q3:", q3)

# Q4: ["ai", "robot", "ml"] ko uppercase list me convert karo.
# Expected: ["AI", "ROBOT", "ML"]
# TODO:
tech = ["ai", "robot", "ml"]
q4 = [name for name in tech name.upper()]
# print("Q4:", q4)

# Q5: pairs = [("a", 2), ("b", 1), ("c", 2)]
# Sort by: count descending, then letter ascending
# Expected: [("a", 2), ("c", 2), ("b", 1)]
# TODO:
q5_pairs = [("a", 2), ("b", 1), ("c", 2)]
q5 = sorted(q5_pairs, key= lambda )
# print("Q5:", q5)


# -----------------------------
# Section D: Self-check runner
# -----------------------------

def run_self_check():
    """Uncomment prints above and compare with expected outputs."""
    print("Self-check complete. TODO solutions fill karo, phir mujhe bhejo.")


if __name__ == "__main__":
    run_self_check()