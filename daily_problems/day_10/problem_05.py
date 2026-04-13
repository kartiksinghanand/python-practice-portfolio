from typing import List, Dict


# Day 10 - Problem 5
# Topic: OOP
#
# Task:
# Create a class MetricTracker with methods:
# - add(name, value): add one metric value under that metric name
# - average(name): return average for that metric, or 0.0 if missing
# - summary(): return dict of metric_name -> average
# - reset(): clear everything
#
# Expected behavior for current sample:
# loss average -> 0.6
# acc average -> 0.85
# summary -> {"loss": 0.6, "acc": 0.85}


class MetricTracker:
    def __init__(self):
        self.metrics : Dict[str: list] = {}
        pass
    
    def add(self, name, value):
        if name in self.metrics:
            self.metrics[name] = [value]
        else:
            self.metrics[name] = value
    
    def average(self, name):
        return sum(self.metrics[name])/len(self.metrics[name])
    
    def summary(self):
        return self.metrics
    
    def reset(self):
        self.metrics = {}


if __name__ == "__main__":
    mt = MetricTracker()
    mt.add("loss", 0.8)
    mt.add("loss", 0.4)
    mt.add("acc", 0.9)
    mt.add("acc", 0.8)
    print(mt.average("loss"))
    print(mt.average("acc"))
    print(mt.summary())