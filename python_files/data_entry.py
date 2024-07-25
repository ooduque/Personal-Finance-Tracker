from datetime import datetime

# Define the date format for parsing and formatting dates
date_format = "%d-%m-%Y"
# Dictionary to map user input to transaction categories
CATEGORIES = {"I": "Income", "E": "Expense"}

# Function to get a date from the user
# If default is allowed and no input is given, return today's date
def get_date(prompt, allow_default=False):
    date_str = input(prompt) # Prompt user for a date
    if allow_default and date_str == '':
    #if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    # Try to parse the input date according to the defined format
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:  # Handle invalid date input
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

# Function to get a valid amount from the user
# Prompt user for an amount and convert to float
# Ensure the amount is positive and non-zero
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e: # Handle invalid input or negative amount
        print(e)
        return get_amount()

# Function to get the transaction category from the user
# Return the full name of the category if valid input is given
# Handle invalid category input
def get_category():
    category = input("Enter the category ('I' for income or 'E' for Expenses): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I for income or 'E' for Expense.")
    return get_category

# Function to get a description for the transaction
def get_description():
    return input("Enter a description (optional): ")