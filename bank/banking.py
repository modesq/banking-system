from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self):
        amount = int(input("please enter amount to deposit: \n>"))
        self.balance += amount
        print(
            "\n amount deposited= " + str(amount) + "\nyour balance= " + str(self.balance)
        )

    def withdraw(self):
        amount = int(input("please enter amount to withdraw: \n>"))
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

    def calculate_income_tax(self):
        income = int(input("please enter your yearly income: \n>"))
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

    def get_balance(self):
        return self.balance

    def __str__(self) -> str:
        return "name: " + self.name + " balance: " + self.balance


class saving_account(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()


class running_account(BankAccount):
    def __init__(self, name, balance=0):
        super().__init__(name, balance)

    def __str__(self) -> str:
        return super().__str__()


def welcome():
    print(
        """
----------------------------------------
----------------------------------------
          Welcome To The Bank
****************************************
"""
    )


def services(account: BankAccount):
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
            account.withdraw()
        elif service == "deposit" or service == "2":
            account.deposit()
        elif service == "calculate income tax" or service == "3":
            account.calculate_income_tax()
        elif service == "view balance" or service == "4":
            print("balance: " + account.get_balance())
        elif service == "create a new savings account" or service == "5":
            new_account = saving_account(account.name, account.balance)
            print("new account created " + new_account.__str__())
        elif service == "quit" or service == "6":
            break
        else:
            print("service not supported")


def goodbye():
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
    welcome()
    username = input("please enter your name: \n >")
    balance = int(input("please enter your balance: \n >"))
    user_account = running_account(username, balance)
    services(user_account)
    goodbye()
