from typing import List, Dict


# Day 6 - Problem 4
# Topic: Parsing
#
# Each line looks like:
# "name=Aman|city=Delhi|role=Engineer"
#
# Task:
# Write parse_profiles(lines) that returns a list of dictionaries.
#
# Important:
# - split each line by "|"
# - split valid parts by "="
# - ignore malformed parts only
# - keep each line as a separate dictionary


lines = [
    "name=Aman|city=Delhi|role=Engineer",
    "name=Diya|city=Mumbai|role=Designer",
    "name=Eshan|badpart|role=Analyst",
]


def parse_profiles(lines: List[str]) -> List[Dict[str, str]]:
    final_summary = []
    for line in lines:
        profiles: Dict[str,int] = {}
        tokens = line.split("|")
        for token in tokens:
            if "=" in token:
                x, y = token.split("=")
                profiles[x] = y
            else:
                continue
        final_summary.append(profiles)
    return final_summary


if __name__ == "__main__":
    print(parse_profiles(lines))
