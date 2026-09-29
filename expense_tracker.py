import csv
import os

FILE_NAME = "expenses.csv"


# 1. Add Expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# 2. View Expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


# 3. Calculate Total Expenses
def calculate_total():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print("\nTotal Expenses:", total)


# 4. Category-wise Spending
def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n--- Category-wise Spending ---")

    for category, amount in categories.items():
        print(category, ":", amount)


# 5. Find Highest Expense
def highest_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    highest = 0
    highest_category = ""
    highest_description = ""

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["Amount"])

            if amount > highest:
                highest = amount
                highest_category = row["Category"]
                highest_description = row["Description"]

    print("\n--- Highest Expense ---")
    print("Category:", highest_category)
    print("Amount:", highest)
    print("Description:", highest_description)


# Main Menu
while True:

    print("\n==============================")
    print("     PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category-wise Spending")
    print("5. Highest Expense")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        print("\nThank you for using Personal Expense Tracker!")
        break

    else:
        print("\nInvalid choice. Please enter 1-6.")