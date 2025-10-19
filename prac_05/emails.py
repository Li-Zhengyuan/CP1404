"""
Emails
Estimate: 30 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        email = input("Email: ")




def extract_name(email):
    name_part = email.split("@")
    parts = name_part.split(".")
    name = " ".join(parts).title()
    return name



main()