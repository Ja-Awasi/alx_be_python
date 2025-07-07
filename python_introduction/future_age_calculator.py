# Prompt the user to input their current age
# The input() function reads a line from input and converts it to a string.
# The int() function converts that string to an integer.
current_age = int(input("How old are you? "))

# Assume the current year is 2023.
# The year 2050 is 2050 - 2023 = 27 years from now.
years_to_add = 27

# Calculate how old the user will be in 2050
age_in_2050 = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {age_in_2050} years old.")