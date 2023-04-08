"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def get_income_input(month_num):
    """Get income input for a given month number."""
    income = float(input(f"Enter income for month {month_num}: "))
    return income


def print_income_report(incomes):
    """Print an income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    income_list = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        income_list.append(income)

    print_income_report(income_list)


main()
