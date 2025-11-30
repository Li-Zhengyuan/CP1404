"""
Time estimation
Plan time:    60 min
Actual time: 120 min
"""

from project import Project

from operator import attrgetter

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
            filename = input("Enter filename to load projects from: ").strip()
            projects = load_file(filename)
        elif choice == "S":
            filename = input("Enter filename to save to: ").strip()
            save_file(filename, projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
    if save_choice in ("y", "yes"):
        save_file(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


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


def save_file(filename, projects):
    """Save the list of project objects to the assigned file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_project(projects):
    """Display incomplete and completed projects, both sorted by priority."""
    incomplete = sorted([project for project in projects if not project.is_complete()], key=attrgetter("priority"))
    complete = sorted([project for project in projects if project.is_complete()], key=attrgetter("priority"))

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Input a date and show projects starting after that date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered, key=attrgetter("start_date")):
        print(project)


def add_new_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project's priority or completion percentage."""
    for i, project in enumerate(projects, 1):
        print(f"{i} {project}")
    choice = int(input("Project choice: ")) - 1
    project_to_update = projects[choice]
    print(project_to_update)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage != "":
        project_to_update.completion_percentage = int(new_percentage)
    if new_priority != "":
        project_to_update.priority = int(new_priority)


main()