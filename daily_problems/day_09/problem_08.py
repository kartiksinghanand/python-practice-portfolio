from typing import List, Dict


# Day 9 - Problem 8
# Topic: Sequence labeling prep
#
# Task:
# Given token records, return only the token texts in order.
#
# Important:
# - keep original order
# - return [] for empty input
#
# Expected output for current sample:
# ["Ethereum", "price", "will", "rise"]


tokens = [
    {"text": "Ethereum", "label": "ASSET"},
    {"text": "price", "label": "METRIC"},
    {"text": "will", "label": "O"},
    {"text": "rise", "label": "ACTION"},
]

def token_texts(tokens: List[Dict]) -> List[str]:
    text = [] 
    if len(tokens) == 0:
        return []
    for token in tokens:
        text.append(token["text"])
    return text       
if __name__ == "__main__":
    print(token_texts(tokens))
