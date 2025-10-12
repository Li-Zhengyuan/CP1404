"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month = int(input("How many months? "))
    print()

    for month in range(1, month + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    display_income_report(incomes, month)


def display_income_report(incomes, month):
    """Display income report for given incomes and number of months."""
    total = 0
    for month in range(1, month + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}         Total: ${total:10.2f}")


main()