from typing import List, Dict


# Day 9 - Problem 3
# Topic: Prediction report
#
# Task:
# Given prediction records, return:
# {
#   "correct": <int>,
#   "incorrect": <int>,
#   "accuracy": <float>
# }
#
# A prediction is correct if:
# prediction == actual
#
# Important:
# - accuracy = correct / total_records
# - if input is empty, accuracy should be 0.0
#
# Expected output for current sample:
# {"correct": 3, "incorrect": 1, "accuracy": 0.75}


# predictions = [
#     {"prediction": 1, "actual": 1},
#     {"prediction": 0, "actual": 1},
#     {"prediction": 1, "actual": 1},
#     {"prediction": 0, "actual": 0},
# ]

predictions = [
    
]

def prediction_report(predictions: List[Dict]) -> Dict[str, float]:
    correct = 0
    for prediction in predictions:
        if prediction["prediction"] == prediction["actual"]:
            correct += 1
    accuracy = 0
    
    if len(predictions) == 0:
        return {"correct": correct, "incorrect": (len(predictions)-correct), "accuracy": 0.0}
         
    else: 
        accuracy = correct/len(predictions)

    return {"correct": correct, "incorrect": (len(predictions)-correct), "accuracy": accuracy}

if __name__ == "__main__":
    print(prediction_report(predictions))
