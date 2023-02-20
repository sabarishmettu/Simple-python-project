# Bank App in Python

#Define the Account Class
class Account:
    #constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited in {self.name}'s account")

    #withdraw method
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn from {self.name}'s account")
        else:
            print(f"Insufficient balance in {self.name}'s account")

#Main function for the bank app
def main():
    #create an account
    my_account = Account('John', 1000)
    print(f"Name: {my_account.name}")
    print(f"Balance: {my_account.balance}")

    #deposit some money
    my_account.deposit(500)

    #withdraw some money
    my_account.withdraw(2000)

#call main function
main()
