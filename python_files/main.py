import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt

# Class to handle CSV file operations
class CSV:
    CSV_FILE = "csv_load/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    # Initializes the CSV file if it doesn't exist
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    # Adds a new entry to the CSV file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline ="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    # Retrieves transactions within a specified date range
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction found in the given date range")
        else:
            print(
                f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)} "
                )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                    )
                )
            
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("Summary")
            print(f"Total Income: £{total_income:.2f}")
            print(f"Total_expense: £{total_expense:.2f}")
            print(f"Net Savings: £{(total_income - total_expense):.2f}")

        return filtered_df

    # Deletes an entry from the CSV file by row ID
    @classmethod
    def delete_entry(cls, row_id):
        df = pd.read_csv(cls.CSV_FILE)
        if 0 <= row_id < len(df):
            df = df.drop(row_id)
            df.to_csv(cls.CSV_FILE, index=False)
            print("Entry deleted successfully.")
        else:
            print("Invalid row ID. No entry deleted.")

    # Updates an entry in the CSV file by row ID
    @classmethod
    def update_entry(cls, row_id, date=None, amount=None, category=None, description=None):
        df = pd.read_csv(cls.CSV_FILE)
        if 0 <= row_id < len(df):
            if date:
                df.at[row_id, "date"] = date
            if amount:
                df.at[row_id, "amount"] = amount
            if category:
                df.at[row_id, "category"] = category
            if description:
                df.at[row_id, "description"] = description
            df.to_csv(cls.CSV_FILE, index=False)
            print("Entry updated successfully.")
        else:
            print("Invalid row ID. No entry updated.")

# Function to add a new transaction
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

# Function to plot income and expense over time
def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = df[df["category"] == "Income"].resample("D").sum(numeric_only=True).reindex(df.index, fill_value=0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum(numeric_only=True).reindex(df.index, fill_value=0)

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to handle the user interface and input
def main():
    while True:
        print("\n1. Add a new transaction")
        print ("2. View transactions and summary within a date range")
        print ("3. Delete a transaction")
        print ("4. Update a transaction")
        print ("5. Exit")
        choice = input("Enter your choice 1-5: ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot?(y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            row_id = int(input("Enter the row ID of the transaction to delete: "))
            CSV.delete_entry(row_id)
        elif choice == "4":
            row_id = int(input("Enter the row ID of the transaction to update: "))
            date = get_date("Enter the new date (dd-mm-yyyy) or press Enter to skip: ", allow_default=False) or None
            amount = get_amount() or None
            category = get_category() or None
            description = get_description() or None
            CSV.update_entry(row_id, date, amount, category, description)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
