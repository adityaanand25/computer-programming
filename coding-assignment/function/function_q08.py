# Create an expense tracker that allows users to add expenses and calculate total spending.

expenses = []
def add_expense(amount, description):
    expenses.append({'amount': amount, 'description': description})
def total_expenses():
    return sum(expense['amount'] for expense in expenses)
add_expense(10, "Coffee")
add_expense(20, "Lunch")
print(f"Total Expenses: ${total_expenses()}")
