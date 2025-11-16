"""
Programming_language
Estimate: 30 minutes
Current Time: 18:16
Actual:   34 minutes
"""

class ProgrammingLanguage:
    """Programming language class."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a Programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """Determine if this programming language is dynamic."""
        return self.typing == "Dynamic"


    def __str__(self):
        """Return a string representation of this programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
