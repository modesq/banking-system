from urllib.request import AbstractBasicAuthHandler
import pytest
from bank.banking import BankAccount, Running_account, Saving_account

bank_account = Running_account("jack", 50)

def test_deposit_integer():
    actual = bank_account.deposit(25)
    excepted = 75
    assert actual == excepted

def test_deposit_string():
    actual = bank_account.deposit("15")
    excepted = 90
    assert actual == excepted

def test_withdraw_integer():
    actual = bank_account.withdraw(15)
    excepted = 75
    assert actual == excepted

def test_withdraw_string():
    actual = bank_account.withdraw("25")
    excepted = 50
    assert actual == excepted

def test_calculate_income_tax_integer():
    actual = bank_account.calculate_income_tax(5000)
    excepted = 0
    assert actual == excepted

def test_creating_new_savings_account():
    actual = Saving_account("rose", 1000)
    excepted = actual.__str__()
    assert excepted == "name: rose - balance: 1000"

def test_creating_new_running_account():
    actual = Running_account("obi wan", 66)
    excepted = actual.__str__()
    assert excepted == "name: obi wan - balance: 66"