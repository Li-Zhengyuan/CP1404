"""
CP1404/CP5632 - Practical
Program to get password and print stars
"""


MINIMUM_LENGTH = 6


def main():
    password = get_password()

    print_asterisks(password)


def get_password():
    """Get user input password continuously until it is valid."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Length of password does not match.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks."""
    print("*" * len(password))


main()