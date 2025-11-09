"""
Time estimation
Plan time:    60 min
Actual time:     min
"""

from project import Project

import datetime

FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = load_file(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":

        elif choice == "S":

        elif choice == "D":

        elif choice == "F":

        elif choice == "A":

        elif choice == "U":

        else:
            print("Invalid option")

        print()
        print(MENU)
        choice = input(">>> ").upper()


def load_file(filename):
    """Load file from a text file and return a list of project objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def s():

main()