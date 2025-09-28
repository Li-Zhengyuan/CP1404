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
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice")

    choice = input("> ").upper()


main()