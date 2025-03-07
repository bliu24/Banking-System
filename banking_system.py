import csv
import uuid
import os
import re

class BankAccount:
    def __init__(self, account_id, name, balance):
        self.account_id = account_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a valid number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdrawal amount must be a valid number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, recipient, amount):
        if recipient is None:
            raise ValueError("Recipient account does not exist.")
        self.withdraw(amount)  # Validates amount and balance
        recipient.deposit(amount)

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.filename = "accounts.csv"
        self.load_accounts()

    def create_account(self, name, initial_balance):
        if not is_valid_name(name):
            raise ValueError("Invalid name. Only letters and spaces allowed.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        account_id = str(uuid.uuid4())
        self.accounts[account_id] = BankAccount(account_id, name, initial_balance)
        self.save_accounts()
        return account_id

    def get_account_by_id(self, account_id):
        return self.accounts.get(account_id)

    def save_accounts(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["account_id", "name", "balance"])
            for account in self.accounts.values():
                writer.writerow([account.account_id, account.name, account.balance])

    def load_accounts(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                account_id, name, balance = row
                self.accounts[account_id] = BankAccount(account_id, name, float(balance))

def is_valid_name(name: str) -> bool:
    return bool(re.match("^[A-Za-z\s]+$", name))

def is_valid_amount(amount: str) -> bool:
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False

def main():
    bank = BankSystem()

    while True:
        print("\nBANKING SYSTEM MENU")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View Account Balance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                name = input("Enter your name (letters and spaces only): ").strip()
                if not is_valid_name(name):
                    print("Invalid name. Please enter a name with letters and spaces only.")
                    continue
                break

            while True:
                initial_balance = input("Enter initial balance: ")
                if is_valid_amount(initial_balance):
                    initial_balance = float(initial_balance)
                    try:
                        account_id = bank.create_account(name, initial_balance)
                        print(f"Account created! Your Account ID: {account_id}")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")
                        break
                else:
                    print("Invalid amount. Please enter a valid positive number.")

        elif choice == "2":
            account_id = input("Enter your Account ID: ")
            amount = input("Enter deposit amount: ")

            if is_valid_amount(amount):
                account = bank.get_account_by_id(account_id)
                if account:
                    try:
                        account.deposit(float(amount))
                        bank.save_accounts()
                        print(f"Deposit successful! New balance: {account.balance}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Account not found.")
            else:
                print("Invalid deposit amount. Please enter a valid positive number.")

        elif choice == "3":
            account_id = input("Enter your Account ID: ")
            amount = input("Enter withdrawal amount: ")

            if is_valid_amount(amount):
                account = bank.get_account_by_id(account_id)
                if account:
                    try:
                        account.withdraw(float(amount))
                        bank.save_accounts()
                        print(f"Withdrawal successful! New balance: {account.balance}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Account not found.")
            else:
                print("Invalid withdrawal amount. Please enter a valid positive number.")

        elif choice == "4":
            sender_id = input("Enter your Account ID: ")
            receiver_id = input("Enter recipient's Account ID: ")
            amount = input("Enter transfer amount: ")

            if is_valid_amount(amount):
                sender = bank.get_account_by_id(sender_id)
                receiver = bank.get_account_by_id(receiver_id)

                if sender and receiver:
                    try:
                        sender.transfer(receiver, float(amount))
                        bank.save_accounts()
                        print(f"Transfer successful! Your new balance: {sender.balance}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("One or both accounts not found.")
            else:
                print("Invalid transfer amount. Please enter a valid positive number.")

        elif choice == "5":
            account_id = input("Enter your Account ID: ")
            account = bank.get_account_by_id(account_id)
            if account:
                print(f"Account Balance for {account.name}: ${account.balance}")
            else:
                print("Account not found.")

        elif choice == "6":
            print("Exiting the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()