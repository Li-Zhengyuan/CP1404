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