"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """"""
    subject_data = load_subject_data(FILENAME)
    print(subject_data)
    display_subject_details(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_records.append(parts)
    input_file.close()
    return subject_records


def display_subject_details(subject_records):
    """"""
    name_width = max(len(record[1]) for record in subject_records)
    count_width = max(len(str(record[2])) for record in subject_records)
    for subject_code, lecturer_name, student_count in subject_records:
        print(f"{subject_code} is taught by {lecturer_name:<{name_width}} and has {student_count:>{count_width}} students")

main()