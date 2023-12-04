class Application:
    def __init__(self, bank):
        self.bank = bank

    def show_main_menu(self):
        while True:
            print("1. Select Account")
            print("2. Open Account")
            print("3. Exit")

            # Display available account numbers
            print("Available Account Numbers:")
            for account in self.bank.accounts:
                print(account.account_number)

            choice = input("Enter your choice: ")

            if choice == '1':
                account_number = input("Enter account number: ")
                account = self.bank.search_account(account_number)
                if account:
                    self.show_account_menu(account)
                else:
                    print("Account not found.")

            elif choice == '2':
                print("This functionality is not implemented yet.")

            elif choice == '3':
                print("Exiting the application...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    def show_account_menu(self, account):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")

            if choice == '1':
                print(f"Current Balance: {account.check_balance()}")

            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print("Deposit successful.")

            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")

            elif choice == '4':
                print("Exiting account menu...")
                break

    def run(self):
        self.show_main_menu()

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = []  # Initialize an empty list to store accounts

    def populate_accounts(self):
        # Hardcoded creation of sample accounts
        self.accounts.append(ChequingAccount("CHQ001", 1000, 5000))
        self.accounts.append(ChequingAccount("CHQ002", 3000, 6000))
        self.accounts.append(ChequingAccount("CHQ003", 5000, 7000))

        self.accounts.append(SavingsAccount("SVG001", 7000, 4000))
        self.accounts.append(SavingsAccount("BNK002", 10000, 6000))
        self.accounts.append(SavingsAccount("BNK003", 12000, 8000))

    def search_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

class SavingsAccount(Account):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            return True
        return False

class ChequingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return True
        return False

# Sample run
if __name__ == "__main__":
    my_bank = Bank()
    my_bank.populate_accounts()
    my_app = Application(my_bank)
    my_app.run()
