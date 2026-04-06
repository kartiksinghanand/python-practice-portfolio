from typing import List, Dict


# Day 5 - Problem 9
# Topic: Nested parsing
#
# Task:
# Each line looks like:
# "name=Aman,age=29,role=engineer"
#
# Write parse_people(lines) that returns list of dicts.
# Ignore malformed key-value pairs safely.
#
# Important:
# - process each line independently
# - split each line by ","
# - then split each valid part by "="
# - if one part is malformed, skip only that part, not the whole line


lines = [
    "name=Aman,age=29,role=engineer",
    "name=Diya,age=25,role=designer",
    "name=Eshan,badpart,role=analyst",
]


def parse_people(lines: List[str]) -> List[Dict[str, str]]:
    
    list_of_infos: List[Dict[str, str]] = []
    for line in lines:
        info = {}
        tokens = line.split(",")
        # print("Tokens: ",tokens)
        for token in tokens:
            if "=" in token:        
                x, y = token.split("=")
                info[x] = y
            else:
                continue
        list_of_infos.append(info)
    return list_of_infos

if __name__ == "__main__":
    print(parse_people(lines))
