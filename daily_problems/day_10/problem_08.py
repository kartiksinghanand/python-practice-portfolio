from typing import List, Dict


# Day 10 - Problem 8
# Topic: Product-style ETL task
#
# Task:
# Given raw prediction records, return cleaned records containing only valid entries.
#
# A record is valid only if it contains:
# - "id"
# - "score"
# - "label"
#
# Return a new list of dictionaries with only these keys:
# - id
# - score
# - label
#
# Expected output for current sample:
# [
#   {"id": "P1", "score": 0.91, "label": 1},
#   {"id": "P3", "score": 0.33, "label": 0}
# ]


records = [
    {"id": "P1", "score": 0.91, "label": 1, "meta": "x"},
    {"id": "P2", "score": 0.76},
    {"id": "P3", "score": 0.33, "label": 0, "extra": 99},
]


def clean_prediction_records(records: List[Dict]) -> List[Dict]:
    valid_records = []
    for record in records:
        keys = record.keys()
        if "id" in keys and "score" in keys and "label" in keys:
            valid_records.append(record)
        else:
            continue
    return valid_records

if __name__ == "__main__":
    print(clean_prediction_records(records))
