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
        current_year = 2022
        return current_year - self.year