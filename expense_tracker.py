from expense import Expense # refers to expense class
import calendar
from datetime import datetime

def main(): # when the main function is run it will run all the below functions in order
    print(f"Running Expense Tracker!")  # checks that main is running properly
    expense_file_path = "expenses.csv"  # creating the csv file
    budget = 2000

    # Each part will be a function to simplify the code and allow for easier debugging

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"📝 Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    # list of categories for user to choose from
    expense_categories = [
        "🍣 Food",
        "🏋️ Fitness",
        "✏️ School",
        "🏖️ Fun",
        "🚗 Transportation",
        "🏷️ Misc"
    ]

    while True:
        print("Select a category: ")
        element_index = 1
        for element in expense_categories:
            print(f"{element_index}. {element}")
            element_index += 1

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        # creates and returns a new Expense object based on user input if selected index is within the preset range
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please try again!")

def save_expense_to_file(expense, expense_file_path):
    print(f"📂 Saving User Expense: {expense} to {expense_file_path}.")
    with open(expense_file_path, "a", encoding="utf-8") as f: # Opens a file for appending data.  If file does not exist, it creates a one.
        f.write(f"{expense.name},{expense.amount},{expense.category}\n") # Writes a line of text to the file

def summarize_expenses(expense_file_path, budget):
    print(f"📊 Summarizing User Expense!")
    expenses = [] # list of objects
    with open(expense_file_path, "r", encoding="utf-8") as f: # r stands for read only mode
        lines = f.readlines()   # Reads all lines from the file into a list, where each line is a string
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",") # strips then splits line into 3
            line_expense = Expense(     # Creates an Expense object using the extracted values.
                name=expense_name, amount=float(expense_amount), category=expense_category
            )       # line_expense is a variable that holds an instance (or object)  of the Expense class.
            expenses.append(line_expense) # once file is read, append to expenses list

    amount_by_category = {}     # creating a dictionary
    for expense in expenses:    # Iterates over each Expense object in the expenses list.
        key = expense.category  # Uses the category of the current expense as the dictionary key.
        if key in amount_by_category:   # Checks if the category is already in the dictionary.
            amount_by_category[key] += expense.amount # Each key is unique within the dictionary, and each key is associated with a value
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category: ")
    for key, amount in amount_by_category.items():  # Iterates over each key-value pair in the dictionary.
        print(f"    {key}: ${amount:.2f}")              # Dictionaries have a key and an associated value, which is why we say for key and amount

    total_spent = sum([expense.amount for expense in expenses]) # for every expense in the expense list, add item to a new list that is the expense amount, then sum it
    print(f"💰 Total spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget/remaining_days
    print(f"👉 Budget Per Day: ${daily_budget:.2f}")


# ensures that the code runs only when we run this file, not when in other files
if __name__ == "__main__":   # will only be true if we run the file directly
    main()

