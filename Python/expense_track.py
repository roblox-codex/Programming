class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully!")

    def remove_expense(self, expense):
        if expense in self.expenses:
            self.expenses.remove(expense)
            print("Expense removed successfully!")
        else:
            print("Expense not found in the tracker!")

    def calculate_total_expenses(self):
        total = sum(self.expenses)
        print(f"Total expenses: ${total}")

    def display_expenses(self):
        if self.expenses:
            print("Expenses:")
            for expense in self.expenses:
                print(f"- ${expense}")
        else:
            print("No expenses found!")

def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. Calculate total expenses")
        print("4. Display expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            expense = float(input("Enter expense amount: "))
            expense_tracker.add_expense(expense)
        elif choice == "2":
            expense = float(input("Enter expense to remove: "))
            expense_tracker.remove_expense(expense)
        elif choice == "3":
            expense_tracker.calculate_total_expenses()
        elif choice == "4":
            expense_tracker.display_expenses()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
