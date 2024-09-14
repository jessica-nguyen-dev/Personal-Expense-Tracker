from expense import Expense # refers to expense class

def main(): # when the main function is run it will run all the below functions in order
    print(f"Running Expense Tracker!")  # checks that main is running properly
    expense_file_path = "expenses.csv"  # creating the csv file

    # Each part will be a function to simplify the code and allow for easier debugging

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path)


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

def summarize_expenses(expense_file_path):
    print(f"📊 Summarizing User Expense!")
    expenses = []
    with open(expense_file_path, "r", encoding="utf-8") as f: # r stands for read only mode
        lines = f.readlines()   # creates a list of strings where each item corresponds to a line in the CSV file
        for line in lines:
            stripped_line = line.strip()    # removes spaces, newlines, trailing whitespaces etc
# ensures that the code runs only when we run this file, not when in other files
if __name__ == "__main__":   # will only be true if we run the file directly
    main()

