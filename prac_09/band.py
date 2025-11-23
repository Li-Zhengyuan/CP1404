class Band:
    """Band class stores a band name and its musicians."""
    def __init__(self, name):
        """Initialise a Band with a name and a list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the Band."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"
