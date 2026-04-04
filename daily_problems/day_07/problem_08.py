from typing import List, Dict, Tuple


# Day 7 - Problem 8
# Topic: Top item selection
#
# Task:
# Given a list of marks records, return the student with the highest total marks
# as a tuple: (student_name, total_marks)
#
# Important:
# - first aggregate marks by student
# - then return the top student
# - if input is empty, return None
#
# What to return:
# - a tuple: (student_name, total_marks)
#
# Expected output for current sample:
# ("Aman", 90)


marks = [
    {"student": "Aman", "marks": 70},
    {"student": "Diya", "marks": 90},
    {"student": "Aman", "marks": 20},
    {"student": "Eshan", "marks": 85},
    {"student": "Sanju", "marks": 100},
]


def top_student(marks: List[Dict]) -> Tuple[str, int] | None:
    students_report = {}
    for student in marks:
        if student["student"] not in students_report:
            students_report[student["student"]] = student["marks"]
        else:
            students_report[student["student"]] += student["marks"]
    # print("students_report: ", students_report)
    
    best_student = max(students_report, key = students_report.get)
    # print("Best student: ", best_student)
    return (best_student,students_report[best_student])
if __name__ == "__main__":
    print(top_student(marks))
