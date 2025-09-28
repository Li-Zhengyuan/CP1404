"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    category = determine_category(score)

    print(f"Score status: {category}")


def determine_category(score):
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