import json
import random
path=r"D:\MAAB academy new\python\homework\lesson-8\homework\accounts.txt"

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self):
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        account_number = random.randint(10000, 99999)
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)
        
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created! Account Number: {account_number}")

    def view_account(self):
        account_number = int(input("Enter account number: "))
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open(path, "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)

    def load_from_file(self):
        try:
            with open(path, "r") as file:
                data = json.load(file)
                self.accounts = {int(acc): Account(**details) for acc, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

# Main loop
bank = Bank()
while True:
    print("\n1. Create Account\n2. View Account\n3. Deposit Money\n4. Withdraw Money\n5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.view_account()
    elif choice == "3":
        bank.deposit()
    elif choice == "4":
        bank.withdraw()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
