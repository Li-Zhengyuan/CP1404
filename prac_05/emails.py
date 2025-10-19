"""
Emails
Estimate: 30 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        answer = input(f"Is your name {name}? (Y/n)").upper()
        if answer not in ("Y", ""):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    name_part = email.split("@")[0]
    parts = name_part.split(".")
    name = " ".join(parts).title()
    return name



main()