from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    print()
    name = input("Name: ")