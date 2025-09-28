MINIMUM_LENGTH = 6


def main():
    password = get_password()

    print_asterisks(password)


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Length of password does not match.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()