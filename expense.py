# The Expense class is a blueprint for creating expense objects with a name, category, and amount. When a new expense is
# created, the __init__ method initializes these attributes (__init__ is short for "initialize").

class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

# The __repr__ method is customized to give a concise and user-friendly description of the expense, which is much easier
# to understand and analyze than the default output (__repr__ is short for "representation").

    def __repr__(self):
        return f"<Expense: {self.name} - {self.category} - ${self.amount:.2f}>"