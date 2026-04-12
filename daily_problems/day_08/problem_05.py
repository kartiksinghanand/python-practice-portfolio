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


# runs = [
#     {"name": "run_1", "accuracy": 0.82},
#     {"name": "run_2", "accuracy": 0.76},
#     {"name": "run_3", "accuracy": 0.91},
#     {"name": "run_4", "accuracy": 0.65},
# ]
runs = [
    {"name": "run_1", "accuracy": 0.2},
    {"name": "run_2", "accuracy": 0.16},
    {"name": "run_3", "accuracy": 0.98},
    {"name": "run_4", "accuracy": 0.3},
]


def experiment_summary(runs: List[Dict]) -> Dict[str, float]:
    summary:  Dict[str, float] = {}
    passed_runs = 0
    failed_runs = 0
    max_run = 0
    for run in runs:
        if run["accuracy"] >= 0.8:
            # summary[run["name"]] = run["accuracy"]
            # summary[run["name"]] = run["accuracy"]
            passed_runs += 1
            if run["accuracy"] > max_run:
                max_run = run["accuracy"]
        else:
            failed_runs += 1
            if run["accuracy"] > max_run:
                max_run = run["accuracy"]
    return {"passed_runs": passed_runs, "failed_runs": failed_runs, "best_accuracy": max_run}
if __name__ == "__main__":
    print(experiment_summary(runs))
