class BankAccount:
    def __init__(self, account_number, balance=0): # The user's account number and their balance
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): # This is the function that lets a user deposit stuff.
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): # This is the function that lets a user withdraw stuff.
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self): # This just prints the user's balance.
        return self.balance

def create_account(): # This is the function that lets the user create an account.
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main():
    accounts = {}
    while True: # This prints at the beginning and asks a user what they want to do.
        print("\n1. Create Account") 
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") # This is the input that asks the user.
        
        if choice == '1': # if the choice is 1 then it runs the create account function which lets them create an account.
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: # This runs if the choice is anything but 1.
            account_number = input("Enter account number: ") # asks the user for their account number.
            if account_number in accounts: # checks to see if the account number exists.
                account = accounts[account_number]
                if choice == '2': # if the choice is 2 then it runs the deposit function.
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount): # checks to see if the deposit amount is a number.
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3': # if the choice is 3 then it runs the withdraw function.
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount): # this if statement checks to see if the user has enough money to withdraw.
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") # if it isn't 1 2 3 or 4, then it just prints the account balance.
            else:
                print("Account not found.") # if 1, 2, 3, 4, 5 wasn't typed, this just prints.
        
        elif choice == '5': # if the choice is 5 meaning they want to exit, it prints this.
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") # if the user didn't type any of the numbers, it prints this.

if __name__ == "__main__":
    main() # runs the function.