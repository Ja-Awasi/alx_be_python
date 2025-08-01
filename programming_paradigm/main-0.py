# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # You can change this starting balance for testing

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    command_args = sys.argv[1].split(':')
    command = command_args[0].lower()

    amount = None
    if len(command_args) > 1:
        try:
            amount = float(command_args[1])
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()