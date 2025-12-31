import csv
import os
from datetime import datetime

# The name of the file where we store data
FILE_NAME = "expenses.csv"

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Asks user for input and saves it to the CSV."""
    date = datetime.now().strftime("%Y-%m-%d") # Auto-get today's date
    print("\n--- Add New Expense ---")
    category = input("Category (Food, Transport, Data, etc): ")
    
    # Error handling loop: keeps asking until user enters a valid number
    while True:
        amount_input = input("Amount (NGN): ")
        if amount_input.replace('.', '', 1).isdigit():
            amount = float(amount_input)
            break
        print("Invalid amount. Please enter a number.")

    desc = input("Description (optional): ") or "No description"

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, desc])
    
    print(" Expense saved successfully!")

def view_expenses():
    """Reads the CSV and prints all expenses."""
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found yet!")
        return

    print("\n--- Your Expenses ---")
    # Formatting: {<width>} creates neat columns
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 60)

    total = 0.0
    
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            # row[0]=Date, row[1]=Category, row[2]=Amount, row[3]=Description
            # We assume the file format is correct
            if len(row) >= 3:
                print(f"{row[0]:<12} | {row[1]:<15} | ₦{row[2]:<9} | {row[3]}")
                total += float(row[2])
    
    print("-" * 60)
    print(f"TOTAL SPENT: ₦{total:,.2f}")

def main():
    """The main program loop."""
    initialize_file()
    
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":

    main()
