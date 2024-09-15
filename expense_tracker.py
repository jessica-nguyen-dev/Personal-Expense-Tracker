# Imports the Expense class from expense.py
# Imports modules for calendar and datetime functions.

from expense import Expense
import calendar
from datetime import datetime

# When the main function is run, it prints a message to confirm that the main function is running, sets the path for the
# CSV file to store expenses, and then defines the budget.
#
# It then executes the functions in order. First it gathers user input for an expense, saves that expense to a CSV file,
# and then summarize the contents of the file.

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 150  # Define the budget

    expense = get_user_expense()

    save_expense_to_file(expense, expense_file_path)
    summarize_expenses(expense_file_path, budget)

# The get_user_expense function prompts the user to enter the details of an expense, including its name and amount, and
# allows them to choose a category from a predefined list. It then creates and returns an Expense object with the entered
# details if the selected category is valid; otherwise, it prompts the user to try again.

def get_user_expense():
    print(f"📝 Getting User Expense!\n")

    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print ("\n")

    expense_categories = [
        "🍣 Food",
        "🏋️ Fitness",
        "✏️ School",
        "🏖️ Fun",
        "🚗 Transportation",
        "🏷️ Misc"
    ]

    while True: # The loop is broken when a valid index is submitted by the user
        print("Select a category: ")
        element_index = 1
        for element in expense_categories:
            print(f"{element_index}. {element}")
            element_index += 1
        print("\n")

        value_range = f"[1 - {len(expense_categories)}]" # Equates to a string (ie 1 - 6)
        selected_index = int(input(f"Enter a category number {value_range}: \n")) - 1
        # Subtracts one because the list index starts at 0, thus is one less than the actual length of the list.

        # Range() stops before the last value (ie range(6) generates indices from 0 to 5).
        # Selected indexes are only from 0 to 5, as we subtract 1 from the users input of 1 to 6 before.

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index] # element of expense categories list at the selected index
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!\n")

# The `save_expense_to_file` function appends the details of the `Expense` object created in the previous function to
# the CSV file. Specifically, it writes the expense's name, amount, and category to the file separated by commas which
# is understood universally by programs such as Microsoft Excel.

# Expense refers to object created and returned by get_user_expense (refer to line 19)

def save_expense_to_file(expense, expense_file_path):
    print(f"📂 Saving User Expense: {expense} to {expense_file_path}.\n")
    with open(expense_file_path, "a", encoding="utf-8") as file: # file is a variable and can be named anything
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")

# The summarize_expenses function reads expenses from a specified CSV file, sums up the total amount spent by
# category, and compares it to a given budget. It then prints a summary of expenses by category, the total amount spent,
# the remaining budget, and calculates the budget per day for the rest of the month.

def summarize_expenses(expense_file_path, budget):

    print(f"📊 Summarizing User Expense!\n")
    expenses = []  # Initializes an empty list to store expense objects line by line from the CSV file we created

    # Opens the file and reads each line. It then splits each line into expense_name, expense_amount, and
    # expense_category, creates an Expense object with these values, and then adds the object to the expenses list.

    with open(expense_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines() # a list of strings
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense( # object
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense) # adds to list of objects

    # Creates a dictionary to track total expenses by category.
    amount_by_category = {}  # Dictionary

    # Iterate through the expenses list and for each expense, update the total for its category in the dictionary,
    # either by adding to an existing total or creating a new entry the category is not already present.

    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount   # adds to value associated with key
        else:
            amount_by_category[key] = expense.amount    # initializes key AND value associated with key

    # Iterates over each key-value pair in the dictionary. Key gets assigned the key of the current item (e.g., "Food").
    # Amount gets assigned the value of the current item (e.g., 150.0)

    print("Expenses By Category: ")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")
    print("\n")

    # Calculate and print the total amount spent and remaining budget
    total_spent = sum([expense.amount for expense in expenses]) # creates a list of all the amount values from the expenses list
    print(f"💰 Total spent: ${total_spent:.2f}")

    # Note: every object in the expenses list called expense and the amount is the value associated with the object?
    # So we are iterating through a list of objects called expenses, where each object is called expense, and amount is
    # an attribute related to an instance of that object.

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    # Calculate and print the daily budget
    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))

def green(text):
    # Apply green color formatting to text
    return f"\033[92m{text}\033[0m"

# Ensure that the code runs only when this file is executed directly
if __name__ == "__main__":
    main()
