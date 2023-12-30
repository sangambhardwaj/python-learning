class BankAccount:

    def __init__(self, my_account_number, my_account_holder_name, my_initial_balance=0):
        self.account_number = my_account_number
        self.account_holder_name = my_account_holder_name
        self.balance = my_initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder_name}: ${self.balance}")

    def update_mobile_number(self, new_mobile_number):
        self.mobile_number = new_mobile_number
        print(f"Mobile number updated to: {self.mobile_number}")


# Example usage:
account1 = BankAccount(my_account_number="123456", my_account_holder_name="John Doe", my_initial_balance=1000)

# account1.display_balance()  # Display initial balance
#
# account1.deposit(500)      # Deposit $500
# account1.withdraw(200)     # Withdraw $200
# account1.display_balance()  # Display updated balance

get_detaills_of_user2 = BankAccount(my_account_number=8738045004, my_account_holder_name="sangam",
                                    my_initial_balance=2300)
get_detaills_of_user2.display_balance()
get_detaills_of_user2.account_holder_name
get_detaills_of_user2.deposit(600)
get_detaills_of_user2.withdraw(500)
get_detaills_of_user2.display_balance()
get_detaills_of_user2.update_mobile_number(87380450087)
