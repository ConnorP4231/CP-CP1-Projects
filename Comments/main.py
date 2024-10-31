class BankAccount:
    def __init__(self, account_number, balance=0):   # defines the users bank account.
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):   # defines if the user wants to deposit money
        if amount > 0:   # checks if it is an actual deposit
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):   # defines if the user wants to withdraw money.
        if 0 < amount <= self.balance:   # checks if the user actually has that amount of money.
            self.balance -= amount
            return True
        return False

    def get_balance(self):   # defines the users account balance.
        return self.balance

def create_account():   # defines the users account number by asking them their number and balance.
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main():   # is the main function to make everything work.
    accounts = {}
    while True:   # gives a list of what the options are.
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':   # if the user types 1 then the code will ask them to create an account.
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']:   
            account_number = input("Enter account number: ")   # checks to see if the user has an account number.
            if account_number in accounts:   # also checks to see if the user has an account number.
                account = accounts[account_number]
                if choice == '2':   # if the user types 2 then it runs the code that asks for the deposit number and adds it to their account.
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()