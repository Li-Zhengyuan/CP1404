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
    print_sorted_guitars(guitars)
    print()

    print("Add new guitars:")
    guitars = add_new_guitar(guitars)

    write_file(guitars, FILENAME)


def load_file(filename):
    """Load data from filename and return a list of Guitar objects."""
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


def print_sorted_guitars(guitars):
    """Print guitars sorted by year."""
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>24} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitar(guitars):
    """Input new guitars to list of Guitar objects."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    return guitars


def write_file(guitars, filename):
    """Write list of Guitar objects to filename."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()