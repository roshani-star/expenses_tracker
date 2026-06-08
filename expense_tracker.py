import json
from datetime import datetime

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except FileNotFoundError:
    expenses = []

while True:

    print("\n" + "=" * 50)
    print("         EXPENSE TRACKER PRO")
    print("=" * 50)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        item = input("Enter expense name: ")
        amount = float(input("Enter amount (₹): "))

        print("\nSelect Category:")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Education")
        print("5. Entertainment")

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Shopping",
            "4": "Education",
            "5": "Entertainment"
        }

        category = categories.get(category_choice, "Other")

        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        expenses.append({
            "item": item,
            "amount": amount,
            "category": category,
            "date_time": current_time
        })

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("\n✅ Expense added successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("\nNo expenses found.")

        else:

            print("\n" + "=" * 90)
            print(f"{'No.':<5}{'Item':<20}{'Amount':<12}{'Category':<15}{'Date & Time'}")
            print("=" * 90)

            for index, expense in enumerate(expenses, start=1):

                print(
                    f"{index:<5}"
                    f"{expense['item']:<20}"
                    f"₹{expense['amount']:<11}"
                    f"{expense['category']:<15}"
                    f"{expense['date_time']}"
                )

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\n💰 Total Spending: ₹{total}")

    elif choice == "4":

        if len(expenses) == 0:
            print("\nNo expenses available.")

        else:

            print("\nExpenses List:")

            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['item']}")

            try:

                delete_index = int(
                    input("\nEnter expense number to delete: ")
                ) - 1

                if 0 <= delete_index < len(expenses):

                    removed = expenses.pop(delete_index)

                    with open("expenses.json", "w") as file:
                        json.dump(expenses, file, indent=4)

                    print(f"\n🗑️ Deleted: {removed['item']}")

                else:
                    print("\n❌ Invalid expense number.")

            except ValueError:
                print("\n❌ Please enter a valid number.")

    elif choice == "5":

        print("\n👋 Thank you for using Expense Tracker Pro!")
        break

    else:
        print("\n❌ Invalid choice! Please try again.")