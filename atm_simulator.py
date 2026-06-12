balance = 10000

pin = int(input("Enter PIN: "))

if pin == 1234:

    print("\n1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")

    choice = int(input("\nEnter Choice: "))

    if choice == 1:

        print("Balance =", balance)

    elif choice == 2:

        amount = int(input("Enter Amount: "))

        if amount <= balance:

            balance -= amount

            print("Money Withdrawn Successfully")

            print("Remaining Balance =", balance)

        else:

            print("Insufficient Balance")

    elif choice == 3:

        amount = int(input("Enter Amount: "))

        balance += amount

        print("Money Deposited Successfully")

        print("Updated Balance =", balance)

    else:

        print("Invalid Choice")

else:

    print("Wrong PIN")