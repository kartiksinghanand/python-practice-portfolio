from typing import List, Dict


# Day 3 - Problem 3
# Topic: Product-style parsing
#
# Task:
# A log line looks like:
# "user=alice action=login status=success"
#
# Write parse_logs(lines) that returns a list of dictionaries.
# Each dictionary should contain the key/value pairs from one line.
#
# Requirements:
# 1) Split each line into parts by spaces
# 2) Split each part into key/value by "="
# 3) Ignore malformed parts safely
# 4) Return [] for empty input
#
# Example:
# ["user=alice action=login status=success"]
# ->
# [{"user": "alice", "action": "login", "status": "success"}]


def parse_logs(lines: List[str]) -> List[Dict[str, str]]:
    logs : List[Dict[str, str]] = []
    for each_line in lines:
        log = {}
        tokens = each_line.split(" ")
        # print("each_line: ",each_line)
        # print("Tokens: ",tokens)
        for each_token in tokens:
            if "=" not in each_token:
                continue
            else:
                token = each_token.split("=")
                log[token[0]] = token[1]
        logs.append(log)



    return logs


if __name__ == "__main__":
    tests = [
        ["user=alice action=login status=success"],
        ["user=bob action=logout", "badpart status=failed"],
        ["user=alice action=login status=success","user=bob action=logout", "badpart status=failed"],
        [],
    ]

    for t in tests:
        print(t, "->", parse_logs(t))
