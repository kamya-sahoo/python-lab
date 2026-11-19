class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, acc_no, balance)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Account")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            account.deposit(amount)
        else:
            print("Enter a valid amount!")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0:
            account.withdraw(amount)
        else:
            print("Enter a valid amount!")

    elif choice == 3:
        account.display()

    elif choice == 4:
        print("Thank you for using Bank System!")
        break

    else:
        print("Invalid choice!")