def main(): # when the main function is run it will run all the below functions in order
    print(f"Running Expense Tracker!")  # checks that main is running properly

    # Each part will be a function to simplify the code

    # Get user input for expense.
    get_user_expense()

    # Write their expense to a file.
    save_expense_to_file()

    # Read file and summarize expenses.
    summarize_expenses()


def get_user_expense():
    print(f"📝 Getting User Expense!")

def save_expense_to_file():
    print(f"📂 Saving User Expense!")

def summarize_expenses():
    print(f"📊 Summarizing User Expense!")

# ensures that the code runs only when we run this file, not when in other files
if __name__ == "__main__":   # will only be true if we run the file directly
    main()

