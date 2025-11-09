CURRENT_YEAR = 2022
AGE_THRESHOLD = 50

class Guitar:
    """Guitar class."""

    def __init__(self, name = "", year = 0, cost = 0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


    def get_age(self):
        """Return how old the guitar is in years."""
        current_year = CURRENT_YEAR
        return current_year - self.year


    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= AGE_THRESHOLD


    def __lt__(self, other):
        """Return True if this guitar is less than another by year."""
        return self.year < other.year