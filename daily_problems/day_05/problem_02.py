from typing import List, Dict


# Day 5 - Problem 2
# Topic: Validation + extraction
#
# Task:
# Given a list of user records, return a list of valid email addresses.
#
# A valid email for this exercise:
# - contains exactly one "@"
# - has at least one character before "@"
# - has at least one "." after "@"
# - the "." must be in the part after "@"
#
# Important:
# - only return the email strings
# - do not return names
# - preserve original input order
#
# Return emails in the same order they appear.


users = [
    {"name": "Aman", "email": "aman@gmail.com"},
    {"name": "Bina", "email": "bina.gmail.com"},
    {"name": "Chirag", "email": "@mail.com"},
    {"name": "Diya", "email": "diya@company"},
    {"name": "Eshan", "email": "eshan@org.in"},
    {"name": "Rohan", "email": "123@org.in"},
]


def valid_emails(users: List[Dict]) -> List[str]:
    emails = []
    for user in users:
        tokens = user["email"].split("@")
        # print(tokens)
        if len(tokens)==2:
            if type(tokens[0]) == type('abc') and len(tokens[0])>=1:
                # print("Pre delete tokens: ",tokens)
                tokens.remove(tokens[0])
                # print("Post delete tokens: ",tokens)
                for token in tokens:
                    dot_tokens = token.split(".")
                    if len(dot_tokens) >=2:
                        emails.append(user["email"])
                        break
                    else:
                        # print("invalid")
                        continue
                    
        # print("tokens: ",tokens) 

    # for user in users:
    #     tokens = user["email"].split("@")
    #     if len(tokens) != 2:
    #         continue
        
    #     if len(tokens[0])>=1:
    #         if float(tokens[0]) != float:
    #             continue
    #         print("valid tokens: ", tokens)  
            
    return emails


if __name__ == "__main__":
    print(valid_emails(users))
