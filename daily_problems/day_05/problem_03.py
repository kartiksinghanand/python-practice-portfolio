from typing import List, Dict


# Day 5 - Problem 3
# Topic: Parsing + reporting
#
# Each API log looks like:
# "endpoint=/login status=200 time=120"
#
# Task:
# Write api_report(logs) that returns:
# {
#   "total_requests": <int>,
#   "success_requests": <int>,   # count only requests with status 200-299
#   "avg_time": <float>          # average time of valid requests only
# }
#
# Requirements:
# - Ignore malformed parts safely
# - Ignore empty lines
# - If no valid requests, avg_time should be 0.0
#
# A request is valid for this exercise only if the line contains all three parts:
# - endpoint=...
# - status=...
# - time=...
#
# Important:
# - total_requests = number of valid requests only
# - success_requests = among valid requests, count only status codes from 200 to 299
# - avg_time = average of time values from valid requests only
# - malformed or incomplete lines should not contribute to any count


logs = [
    "endpoint=/login status=200 time=120",
    "endpoint=/profile status=404 time=80",
    "endpoint=/home status=201 time=100",
    "",
    "badpart status=500",
]


def api_report(logs: List[str]) -> Dict[str, float]:
    report: Dict[str, float] = {}
    ignorables = 0
    success_req = 0
    time_list = []
    for i in logs:
        if len(i) == 0 or "badpart" in i:
            ignorables += 1
        else:
            tokens = i.split(" ")
            a, b = tokens[2].split("=")
            time_list.append(float(b))
    valid_req = len(logs) - ignorables
    # for i in logs:
    #     if len(i)==0 or ("badpart" in i):
    #         ignorables += 1
    # report["total_requests"] = len(logs)
    # report["success_requests"] = len(logs) - ignorables
    # for log in logs:
    #     if len(log) == 0:
    #         time.append(0.0)
    #         break
    #     tokens_log = log.split(" ")
    #     avg_time = tokens_log[2].split("=")
    #     time.append(float(avg_time[1]))
    # # print("time: ", time)
    
    # # print("avg_time: ", sum(time)/len(time))
    # report["avg_time"] = sum(time)/len(time)
    
    for log in logs:
        if len(log) !=0 and "badpart" not in log:
            endpoint, status, time  = log.split(" ")
            s,stat_code = status.split("=")
            t = time.split("=")
            if int(stat_code) <= 299 and int(stat_code) >= 200:
                # time_list.append(float(t[1])) 
                success_req += 1
            # print("log: ",log)
            report["total_requests"] = valid_req
            report["success_requests"] = success_req
            report["avg_time"] = sum(time_list)/len(time_list) 
            # print(report)         
    return report



if __name__ == "__main__":
    print(api_report(logs))
