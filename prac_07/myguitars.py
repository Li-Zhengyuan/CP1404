from guitar import Guitar

def main():
    """Read guitar data, store as Guitar objects, sort, and display."""
    guitars = []

    # Read from CSV
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)

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
        print(f"Guitar {i}: {guitar.name:>25} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()