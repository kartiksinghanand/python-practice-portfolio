from typing import List, Dict


# Day 8 - Problem 5
# Topic: Experiment reporting
#
# Task:
# Given experiment results, return:
# {
#   "passed_runs": <int>,
#   "failed_runs": <int>,
#   "best_accuracy": <float>
# }
#
# Rules:
# - a run passes if accuracy >= 0.80
# - best_accuracy = highest accuracy in the list
# - if input is empty, best_accuracy should be 0.0
#
# What to return:
# - a summary dictionary with the three fields above
#
# Expected output for current sample:
# {"passed_runs": 2, "failed_runs": 2, "best_accuracy": 0.91}


runs = [
    {"name": "run_1", "accuracy": 0.82},
    {"name": "run_2", "accuracy": 0.76},
    {"name": "run_3", "accuracy": 0.91},
    {"name": "run_4", "accuracy": 0.65},
]


def experiment_summary(runs: List[Dict]) -> Dict[str, float]:
    # TODO
    pass


if __name__ == "__main__":
    print(experiment_summary(runs))
