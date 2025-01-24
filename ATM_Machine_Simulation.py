class ATM:
    def __init__(self, pin, balance=0):
        """
        Initialize the ATM with a PIN and Current balance.
        """
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def validate_pin(self):
        """
        Validate the user's PIN. Return True if the PIN is correct,otherwise False.
        """
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def balance_inquiry(self):
        """
        Display Current Account Balance.
        """
        print(f"\nYour current balance is: ${self.balance}")

    def cash_withdrawal(self):
        """
        Allow the user to withdraw cash, if sufficient balance exists.
        """
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount > self.balance:
                print("Insufficient balance!!!")
            else:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful.")
                self.transaction_history.append(f"Withdrew: ${amount}")
        except ValueError:
            print("Invalid amount entered. Please enter a numeric value.")

    def cash_deposit(self):
        """
        Allow the user to deposit cash into their account.
        """
        try:
            amount = float(input("Enter amount to deposit: $"))
            self.balance += amount
            print(f"Deposit of ${amount} successful.")
            self.transaction_history.append(f"Deposited: ${amount}")
        except ValueError:
            print("Invalid amount entered. Please enter a numeric value.")

    def change_pin(self):
        """
        Allow the user to change their PIN with confirmation.
        """
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_pin:
            self.pin = new_pin
            print("PIN changed Successfully.")
        else:
            print("PIN confirmation does not match, Try again.")

    def show_transaction_history(self):
        """
        Display the user's transaction history, if available.
        """
        if not self.transaction_history:
            print("\nNo Transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")


# Simulating the ATM operations
def main():
    # Initialize the ATM with a default PIN and starting balance
    atm = ATM(pin="7777", balance=1000)

    print("Welcome to Your HDFC ATM!")
    if not atm.validate_pin():
        print("Incorrect PIN. For your safety, the session has been terminated.")
        return

    while True:
        # Display the menu options
        print("\nWhat would you like to do today?")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        # Get user input
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            atm.balance_inquiry()
        elif choice == "2":
            atm.cash_withdrawal()
        elif choice == "3":
            atm.cash_deposit()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.show_transaction_history()
        elif choice == "6":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()