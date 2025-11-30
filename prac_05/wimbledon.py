"""
Wimbledon
Estimate: 30 minutes
Actual:   40 minutes
"""

FILENAME = "wimbledon.csv"

def main():
    """"Read Wimbledon data and display champions and countries."""
    records = load_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_result(champion_to_wins, countries)



def load_data(filename):
    """Read CSV data return records as list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        records = [line.strip().split(",") for line in in_file]
    return records



def process_data(records):
    """Count champion's wins and collect unique countries."""
    champion_to_wins = {}
    countries = set()

    for record in records:
        champion = record[2]
        country = record[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1

    return champion_to_wins, countries



def display_result(champion_to_wins, countries):
    """Display champions and countries in format."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))



main()