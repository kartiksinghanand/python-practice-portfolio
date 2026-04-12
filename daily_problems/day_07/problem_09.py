from typing import List, Dict


# Day 7 - Problem 9
# Topic: Requirement-reading practice
#
# Task:
# Given a list of exam records, return:
# {
#   "passed": <int>,
#   "failed": <int>,
#   "top_score": <int>
# }
#
# Rules:
# - pass if score >= 40
# - fail if score < 40
# - top_score should be the highest score in the whole list
# - if input is empty, top_score should be 0
#
# What to return:
# - passed = number of students with score >= 40
# - failed = number of students with score < 40
# - top_score = highest score in the list, or 0 for empty input
#
# Expected output for current sample:
# {"passed": 2, "failed": 2, "top_score": 82}


records = [
    {"name": "Aman", "score": 82},
    {"name": "Diya", "score": 37},
    {"name": "Eshan", "score": 64},
    {"name": "Bina", "score": 21},
]


def exam_summary(records: List[Dict]) -> Dict[str, int]:
    student_summary : Dict[str, int] = {"passed":0, "failed": 0, "top_score": int}
    for record in records:
        if record["score"] >= 40:
            student_summary["passed"] += 1
        elif record["score"] <40:
            student_summary["failed"] += 1
    scores = [i["score"] for i in records]
    student_summary["top_score"] = max(scores)
    return student_summary

if __name__ == "__main__":
    print(exam_summary(records))
