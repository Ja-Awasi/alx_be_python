# finance_calculator.py

# 1. User Input for Financial Details
try:
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
except ValueError:
    print("Invalid input. Please enter numerical values for income and expenses.")
    exit() # Exit the script if input is not a valid number

# 2. Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# 3. Project Annual Savings
annual_interest_rate = 0.05  # 5% simple annual interest rate

# Calculate annual savings before interest
annual_savings_before_interest = monthly_savings * 12

# Calculate the projected savings after one year, incorporating the interest
# Simplified formula: Projected Savings = Annual Savings * (1 + interest_rate)
projected_savings = annual_savings_before_interest * (1 + annual_interest_rate)

# 4. Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.") # .2f for 2 decimal places500