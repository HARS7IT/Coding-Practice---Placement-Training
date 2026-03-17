bank={}

def create_account():
    acc_no = int(input("Enter your account number: "))
    if acc_no in bank:
        print("Bank account already exists!")
    else:
        bank[acc_no]=0
        print("New Account created successfully with balance Rs 0!")


def deposit():
    acc_no=int(input("Enter your account number: "))
    if acc_no in bank:
        amount=float(input("Enter the amount to be deposited: "))
        bank[acc_no]+=amount
        print(f"Amount Deposited: Rs ",amount)
        print(f"Total Bank Balance: Rs ",bank[acc_no])
    else:
        print("Bank account not found!")


def withdraw():
    acc_no=int(input("Enter your account number: "))
    if acc_no in bank:
        w_amount=float(input("Enter the amount to be withdrawn: "))
        if w_amount<=bank[acc_no]:
            bank[acc_no]-=w_amount
            print(f"Amount to be withdrawn: Rs ",w_amount)
            print(f"Total Bank Balance: Rs ",bank[acc_no])
        else:
            print("Insufficient Balance!")
    else:
        print("Account not found!")


def check_balance():
    acc_no=int(input("Enter your account number: "))
    if acc_no in bank:
        print(f"Balance for account {acc_no}: Rs ",bank[acc_no])
    else:
        print("Account not found!")


def menu():
    while True:
        print("\n----- MINI BANKING SYSTEM -----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice! Try again.")


menu()
    