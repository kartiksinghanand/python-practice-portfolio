from typing import List, Dict


# Day 4 - Problem 2
# Topic: Filtering + transformation
#
# Task:
# Given a list of student records, return a list of names of students who:
# - scored at least 75
# - are active
#
# Return names in alphabetical order.


students = [
    {"name": "Aman", "score": 82, "active": True},
    {"name": "Bina", "score": 74, "active": True},
    {"name": "Chirag", "score": 91, "active": False},
    {"name": "Diya", "score": 77, "active": True},
    {"name": "Eshan", "score": 75, "active": True},
]


def eligible_students(students: List[Dict]) -> List[str]:
    students_eligibility = []
    for each_student in students:
        if each_student["score"] >= 75 and each_student["active"] == True:
            students_eligibility.append(each_student["name"])
    
    return students_eligibility
if __name__ == "__main__":
    print(eligible_students(students))
