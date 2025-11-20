# Simple Budget Calculator

# Income variables
salary = 3000
side_income = 500
investment_income = 150

# Expense variables
rent = 1200
groceries = 400
utilities = 150
transportation = 200
entertainment = 100
other_expenses = 150

# Calculate totals
total_income = salary + side_income + investment_income
total_expenses = rent + groceries + utilities + transportation + entertainment + other_expenses

# Calculate balance
balance = total_income - total_expenses

# Display results
print("=== MONTHLY BUDGET ===")
print(f"Total Income: ${total_income}")
print(f"Total Expenses: ${total_expenses}")
print(f"Balance: ${balance}")

if balance > 0:
    print("Great! You have a surplus this month.")
elif balance < 0:
    print("Warning! You have a deficit this month.")
else:
    print("You broke even this month.")