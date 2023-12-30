class BankAccount:

    def __init__(self, name, account_number, mobile_number, address, initial_balance=0):
        # Public attributes
        self.name = name
        self.account_number = account_number
        self.mobile_number = mobile_number
        self.address = address

        # Private variables
        self._balance = initial_balance  # Starting with initial balance

    def get_balance(self):
        """Get the current balance."""
        return self._balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self._balance += amount
            return True
        else:
            print("Invalid deposit amount. Please enter a positive value.")
            return False

    def _validate_withdrawal(self, amount):
        """Private method to validate if withdrawal is possible."""
        if amount > 0 and amount <= self._balance:
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return False

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self._validate_withdrawal(amount):
            self._balance -= amount
            return True
        else:
            return False

    def account_info(self):
        """Get account information."""
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\n" \
               f"Mobile Number: {self.mobile_number}\nAddress: {self.address}\n" \
               f"Current Balance: ${self._balance:.2f}"

    def update_account_info(self, name=None, mobile_number=None, address=None):
        """Update account information."""
        if name:
            self.name = name
        if mobile_number:
            self.mobile_number = mobile_number
        if address:
            self.address = address
        return True


# Example usage:
account = BankAccount("John Doe", "123456789", "555-1234", "123 Main St", initial_balance=1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Print account information
print(account.account_info())

# Update account information
account.update_account_info(name="John Smith", mobile_number="555-5678")

# Print updated account information
print(account.account_info())
print(account.withdraw(400))
print(account.get_balance())
