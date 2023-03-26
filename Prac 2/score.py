"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

user_score = float(input("Enter score: "))
user_status = determine_score_status(user_score)
print(user_status)

random_score = random.randint(0, 100)
print(f"Random score: {random_score}")
random_status = determine_score_status(random_score)
print(random_status)
