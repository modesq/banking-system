from abc import ABC, abstractmethod

# hello there
class BankAccount(ABC):
    """
    abstract class for a bank account to be inherited from witha all of its methods and attributes
    """
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        """
        this method takes an amount that will be added to the balance and returns the new balance
        """
        amount = float(amount)
        self.balance += amount
        print(
            "\n amount deposited= " + str(amount) + "\nyour balance= " + str(self.balance)
        )
        return self.balance

    def withdraw(self, amount: float):
        """
        this method take an amount that will need to be withdrawn and the substraces it from the 
        balance, and then returns the new balance
        """
        amount = float(amount)
        if self.balance < amount:
            print("Not enough balance")
        else:
            print(
                "\namount withdrawn= "
                + str(amount)
                + "\nyour balance= "
                + str(self.balance)
            )
            self.balance -= amount
        return self.balance

    def calculate_income_tax(self, income):
        """
        this method calculates the yearly tax amount depending on yearly income
        """
        if income <= 5000:
            tax = 0
        elif income <= 10000:
            tax = (income - 5000) * 0.05
        elif income <= 15000:
            tax = (income - 10000) * 0.10
        elif income <= 20000:
            tax = (income - 15000) * 0.15
        elif income <= 1000000:
            tax = (income - 20000) * 0.20
        else:
            tax = (income - 1000000) * 0.30
        print("your annual income tax in jordan is", tax, "JODS")
        return tax

    def get_balance(self):
        """
        this method returns the the balance
        """
        return self.balance

    def __str__(self) -> str:
        """
        this method makes a string out of the object attributes
        """
        return "name: " + self.name + " - balance: " + str(self.balance)


class Saving_account(BankAccount):
    """
    this a class that inherits the class BankAccount
    """
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()


class Running_account(BankAccount):
    """
    this a class that inherits the class BankAccount
    """
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()


def welcome():
    """
    this fucntion welcomes the user 
    """
    print(
        """
----------------------------------------
----------------------------------------
          Welcome To The Bank
****************************************
"""
    )


def services(account: BankAccount):
    """
    tjis functional prints the services for the user and calls the other classes and fucntions as needed
    """
    while True:
        print(
            """
****************************************
** please enter the services you need **
** 1. withdraw                        **
** 2. deposit                         **
** 3. calculate income tax            **
** 4. view balance                    **
** 5. create a new savings account    ** 
** 6. enter "Quit" to exit"           **
****************************************
            """
        )
        service = input("Enter service \n>").lower()
        if service == "withdraw" or service == "1":
            try:
                amount = float(input("please enter amount to withdraw: \n>"))
                account.withdraw(amount)  # calling the method withdraw
            except:
                print("please input a number")
        elif service == "deposit" or service == "2":
            try:
                amount = float(input("please enter amount to deposit: \n>"))
                account.deposit(amount) # calling the method deposit
            except:
                print("please input a number")
        elif service == "calculate income tax" or service == "3":
            try:
                income = float(input("please enter your yearly income: \n>"))
                account.calculate_income_tax(income) #calling the calculate_income method
            except:
                print("please input a number")
        elif service == "view balance" or service == "4":
            print("balance: " + account.get_balance()) # calling the method get_balance
        elif service == "create a new savings account" or service == "5":
            new_account = Saving_account(account.name, account.balance) # creating a new savings account
            print("new account created " + new_account.__str__())
        elif service == "quit" or service == "6":
            break #exiting the infinite loop which will close the program after
        else:
            print("service not supported")


def goodbye():
    """
    this fucntion prints a goodbye message to the terminal
    """
    print(
        """
****************************************
    thank you for using this service
            see you soon!!
----------------------------------------
----------------------------------------
"""
    )


if __name__ == "__main__":
    """
    this is the main function which runs the whole program
    """
    welcome()
    username = input("please enter your name: \n >")
    balance = float(input("please enter your balance: \n >"))
    user_account = Running_account(username, balance)
    services(user_account)
    goodbye()
