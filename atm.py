class User:
    def authenticate(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

class ATM:
    def authenticate_user(self, user_id, pin):
        self.users = {
            "user123": {"user_id": "user123", "pin": "1234", "balance": 1000, "transaction_history": []},
            "user456": {"user_id": "user456", "pin": "5678", "balance": 1500, "transaction_history": []},
        }
        
        if user_id in self.users:
            user = self.users[user_id]
            if user["pin"] == pin:
                self.current_user = user
                return True
        return False

    def check_balance(self):
        return self.current_user["balance"]

    def deposit(self, amount):
        if amount > 0:
            self.current_user["balance"] += amount
            self.current_user["transaction_history"].append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.current_user['balance']}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.current_user["balance"]:
            self.current_user["balance"] -= amount
            self.current_user["transaction_history"].append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.current_user['balance']}"
        return "Insufficient funds or invalid withdrawal amount."

    def transfer(self, recipient, amount):
        if recipient in self.users and amount > 0:
            if self.current_user["balance"] >= amount:
                self.current_user["balance"] -= amount
                self.users[recipient]["balance"] += amount
                self.current_user["transaction_history"].append(f"Transferred ${amount} to {recipient}")
                return f"Transferred ${amount} to {recipient}. New balance: ${self.current_user['balance']}"
            return "Insufficient funds to complete the transfer."
        return "Invalid recipient or transfer amount."

    def get_transaction_history(self):
        return self.current_user["transaction_history"]

    def logout(self):
        self.current_user = None

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Authenticate")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Logout")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")
            if atm.authenticate_user(user_id, pin):
                print("Authentication successful.")
            else:
                print("Authentication failed. Invalid User ID or PIN.")
        elif choice == "2":
            if "current_user" in atm.__dict__:
                print(f"Current balance: ${atm.check_balance()}")
            else:
                print("Please authenticate first.")
        elif choice == "3":
            if "current_user" in atm.__dict__:
                amount = float(input("Enter deposit amount: "))
                print(atm.deposit(amount))
            else:
                print("Please authenticate first.")
        elif choice == "4":
            if "current_user" in atm.__dict__:
                amount = float(input("Enter withdrawal amount: "))
                print(atm.withdraw(amount))
            else:
                print("Please authenticate first.")
        elif choice == "5":
            if "current_user" in atm.__dict__:
                recipient = input("Enter recipient's User ID: ")
                amount = float(input("Enter transfer amount: "))
                print(atm.transfer(recipient, amount))
            else:
                print("Please authenticate first.")
        elif choice == "6":
            if "current_user" in atm.__dict__:
                history = atm.get_transaction_history()
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("Please authenticate first.")
        elif choice == "7":
            if "current_user" in atm.__dict__:
                atm.logout()
                print("Logged out successfully.")
            else:
                print("Please authenticate first.")
        elif choice == "8":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

