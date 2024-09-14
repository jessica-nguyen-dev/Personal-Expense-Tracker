def main(): # when the main function is run it will run all the below functions in order
    print(f"Running Expense Tracker!")  # checks that main is running properly

    # Each part will be a function to simplify the code and allow for easier debugging

    # Get user input for expense.
    get_user_expense()

    # Write their expense to a file.
    save_expense_to_file()

    # Read file and summarize expenses.
    summarize_expenses()


def get_user_expense():
    print(f"📝 Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_amount}.")

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

        if selected_index in range(len(expense_categories)):
            break
        else:
            print("Invalid category. Please try again!")



def save_expense_to_file():
    print(f"📂 Saving User Expense!")

def summarize_expenses():
    print(f"📊 Summarizing User Expense!")

# ensures that the code runs only when we run this file, not when in other files
if __name__ == "__main__":   # will only be true if we run the file directly
    main()

