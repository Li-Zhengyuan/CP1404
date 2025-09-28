def main():
    password = input("Enter password: ")

    repeat_password = input("Repeat password: ")
    while len(repeat_password) < len(password):
        print("Length of password does not match.")
        repeat_password = input("Repeat password: ")

    print("*" * len(password))

main()