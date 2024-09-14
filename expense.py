# defines a class named Expense, which is used to represent an expense with three attributes: name, category, and amount

class Expense:      # __init__ constructor is automatically called when a new instance is created
    def __init__(self, name, category, amount) -> None:     # None indicates that this method does not return a value
        self.name = name       # Name, category, and amount are parameters that are passed when a new object is created
        self.category = category
        self.amount = amount

def __repr__(self):     # overwrites default output to something descriptive
    return f"<Expense: {self.name} - {self.category} - ${self.amount:.2f}>"