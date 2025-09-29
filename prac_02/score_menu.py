"""
CP1404/CP5632 - Practical
Program to display a score menu
"""


EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Execute the menu choice until user chooses to quit."""
    score = -1

    print(MENU)
    choice = input(">> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            score = validate_score(score)
            category = determine_category(score)
            print(f"Your score {score} is {category}")
        elif choice == "S":
            score = validate_score(score)
            print("*" * score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">> ").upper()

    print("Farewell")


def get_score():
    """Get the input score."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def validate_score(score):
    """Validate the input score."""
    if score == -1:
        score = get_score()
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