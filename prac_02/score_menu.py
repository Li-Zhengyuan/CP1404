"""
CP1404/CP5632 - Practical
Program to display a score menu
"""


EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = validate_score()

    print(MENU)
    choice = input(">> ").upper()

    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            category = determine_category(score)
            print(f"Your score {score} is {category}")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">> ").upper()

    print("Farewell")


def validate_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_category(score):
    """Determine the category of the score."""
    if score >= EXCELLENT_THRESHOLD:
        category = "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()