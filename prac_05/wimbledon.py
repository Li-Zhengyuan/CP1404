"""
Wimbledon
Estimate: 30 minutes
Actual:    minutes
"""

FILENAME = "wimbledon.csv"

def main():
    pass



def load_data(filename):
    """Read CSV data return records as list."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        records = [line.strip().split(",") for line in in_file]
    return records



main()