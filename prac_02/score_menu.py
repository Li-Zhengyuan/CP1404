"""
CP1404/CP5632 - Practical
Program to display a score menu
"""


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():

    print(MENU)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            category = determine_category(score)
            print(f"Your score is {category}")
        elif choice == "S":
            pass
        else:
            print("Invalid choice")

    choice = input("> ").upper()


def validate_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = input("Enter score: ")
    return score


def determine_category(score):
    """Determine the category of the score."""
    if score >= 90:
        category = "Excellent"
    elif score >= 50:
        category = "Passable"
    else:
        category = "Bad"
    return category


main()