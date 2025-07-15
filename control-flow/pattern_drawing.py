# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Draw the Pattern
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1
# This code will draw a square pattern of asterisks based on the user's input size.
# The outer loop controls the number of rows, and the inner loop prints asterisks in each row.
# The pattern will look like this for size = 3: