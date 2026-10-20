# Daily expenses add karega aur total spending calculate karega.


expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        expenses.append((name, amount))
        print("Expense added successfully!")

    elif choice == "2":
        for name, amount in expenses:
            print(name, ":", amount)

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        print("Total Expenses:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
