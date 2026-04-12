from typing import List, Dict


# Day 8 - Problem 9
# Topic: Inference request validation
#
# Task:
# Given inference request dictionaries, return:
# {
#   "valid_requests": <int>,
#   "invalid_requests": <int>,
#   "model_usage": {"tiny": 2, "base": 1, ...}
# }
#
# A request is valid only if it contains:
# - "model"
# - "prompt"
#
# Important:
# - count model_usage only for valid requests
# - ignore malformed requests safely
#
# Expected output for current sample:
# {"valid_requests": 3, "invalid_requests": 2, "model_usage": {"tiny": 2, "base": 1}}


requests = [
    {"model": "tiny", "prompt": "hello"},
    {"model": "base", "prompt": "summarize this"},
    {"model": "tiny"},
    {},
    {"model": "tiny", "prompt": "forecast"},
]


def inference_summary(requests: List[Dict]) -> Dict[str, object]:
    request_summary: Dict[str, object] = {}
    model_usage = {}
    valid_requests = 0
    invalid_requests = 0
    for request in requests:
        if len(request) == 0 or ("model" and "prompt" not in request):
            invalid_requests += 1 
        else:

            if request["model"] not in model_usage:
                model_usage[request["model"]] = 1    
            else:
                model_usage[request["model"]] += 1
            valid_requests += 1
    request_summary["valid_requests"] = valid_requests 
    request_summary["invalid_requests"] = invalid_requests 
    request_summary["model_usage"] = model_usage
    return request_summary
            

if __name__ == "__main__":
    print(inference_summary(requests))
