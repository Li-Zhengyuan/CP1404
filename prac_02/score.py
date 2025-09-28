"""
CP1404/CP5632 - Practical
Program to determine score status
"""


import random


def main():
    """Print the category of the score and random score."""
    score = float(input("Enter score: "))

    category = determine_category(score)

    print(f"Score status: {category}")

    random_score = random.randint(0, 100)
    print(f"Random score {random_score} is {determine_category(random_score)}")


def determine_category(score):
    """Determine the category of the score."""
    if score < 0 or score > 100:
        category = "Invalid score"
    elif score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()