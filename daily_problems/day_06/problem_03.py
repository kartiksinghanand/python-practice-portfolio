from typing import List, Dict


# Day 6 - Problem 3
# Topic: Validation + counting
#
# Task:
# Given a list of passwords, return a summary:
# {
#   "valid": <int>,
#   "invalid": <int>
# }
#
# A password is valid for this exercise if:
# - length is at least 8
# - it contains at least one digit
#
# Important:
# - count every password exactly once


passwords = ["abc123", "strongpass1", "hello2024", "short", "secure9"]


def password_summary(passwords: List[str]) -> Dict[str, int]:
    valid_passwords = []
    invalid_passwords = []
    summary = {}
    for password in passwords:
        contains_digit = False
        tokens = [alphabet for alphabet in password]
        # print("tokens: ", tokens)
        for i in tokens:
            if len(tokens) >= 8:
                if i in "0123456789":
                        valid_passwords.append(password)
                        break
                else:
                    continue
        else:
            invalid_passwords.append(password)
        # summary["valid_passwords"] = [x for x in passwords if x not in invalid_passwords]
        summary["valid"] = len(valid_passwords)
        summary["invalid"] = len(invalid_passwords)
    return summary


if __name__ == "__main__":
    print(password_summary(passwords))
