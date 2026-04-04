from typing import List, Dict


# Day 7 - Problem 7
# Topic: Parsing + cleanup
#
# Each line looks like:
# "name=Aman;score=82;grade=A"
#
# Task:
# Return a list of dictionaries.
#
# Important:
# - split each line by ";"
# - then split valid parts by "="
# - ignore malformed parts only
# - keep one dictionary per line
#
# What to return:
# - one dictionary per input line
# - if one part is malformed, skip only that part, not the whole line
#
# Expected output for current sample:
# [
#   {"name": "Aman", "score": "82", "grade": "A"},
#   {"name": "Diya", "score": "77", "grade": "B"},
#   {"name": "Eshan", "grade": "A"}
# ]


lines = [
    "name=Aman;score=82;grade=A",
    "name=Diya;score=77;grade=B",
    "name=Eshan;badpart;grade=A",
]


def parse_students(lines: List[str]) -> List[Dict[str, str]]:
    students_data : List[Dict[str, str]] = []

    for line in lines:
        temp ={}
        tokens = line.split(";")
        for token in tokens:
            if "=" in token:
                parts = token.split("=")
                temp[parts[0]] = parts[1]
        students_data.append(temp)
    # print("students_data: ", students_data)
    return students_data
if __name__ == "__main__":
    print(parse_students(lines))
