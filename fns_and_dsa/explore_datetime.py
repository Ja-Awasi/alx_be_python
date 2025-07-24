# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    """
    Calculates and displays a future date based on user input
    """
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()