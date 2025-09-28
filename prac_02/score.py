"""
CP1404/CP5632 - Practical
Program to determine score status
"""

EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

import random


def main():
    """Print the category of the score and random score."""
    score = float(input("Enter score: "))

    category = determine_category(score)

    print(f"Score status: {category}")

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score {random_score} is {determine_category(random_score)}")


def determine_category(score):
    """Determine the category of the score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        category = "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        category = "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()