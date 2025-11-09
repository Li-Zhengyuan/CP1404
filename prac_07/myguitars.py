from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Read guitar data, store as Guitar objects, sort, and display."""
    guitars = load_file(FILENAME)


    print("These are my guitars:")
    for guitar in guitars:
        print(f"{guitar}")
    print()

    guitars.sort()

    print("Sorted by year (oldest to newest):")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>24} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    print("Add new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    # Save all guitars back to the CSV
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def load_file(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


main()