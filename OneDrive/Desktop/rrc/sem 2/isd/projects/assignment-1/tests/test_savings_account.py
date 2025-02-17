
"""
Description: Unit tests for the SavingsAccount class.
Author: Jashanpreet Singh Sidhu
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py

"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.savings_account import SavingsAccount
from datetime import date


class TestSavingsAccount(unittest.TestCase):

    def test_initialization_with_valid_arguments_sets_attributes(self):
        expected = SavingsAccount(100, 100, 100, date(2024, 3, 25), 20)
        self.assertEqual(100, expected._BankAccount__account_number)
        self.assertEqual(100, expected._BankAccount__client_number)
        self.assertEqual(100, expected._BankAccount__balance)
        self.assertEqual(date(2024, 3, 25), expected._date_created)
        self.assertEqual(20, expected._SavingsAccount__minimum_balance)

    def test_initialization_with_invalid_minimum_balance_defaults_to_fifty(self):
        expected = SavingsAccount(100, 100, 100, date(2024, 3, 25), 'twenty')
        self.assertEqual(50, expected._SavingsAccount__minimum_balance)

    def test_service_charge_when_balance_exceeds_minimum_is_base_charge(self):
        expected = SavingsAccount(100, 100, 100, date(2024, 3, 25), 20)
        self.assertEqual(0.50, expected.get_service_charges())

    def test_service_charge_when_balance_equals_minimum_is_base_charge(self):
        expected = SavingsAccount(100, 100, 20, date(2024, 3, 25), 20)
        self.assertEqual(0.50, expected.get_service_charges())

    def test_service_charge_when_balance_is_below_minimum_is_calculated(self):
        expected = SavingsAccount(100, 100, 10, date(2024, 3, 25), 20)
        self.assertEqual(1, expected.get_service_charges())

    def test_string_representation_with_valid_arguments_returns_formatted_output(self):
        expected = SavingsAccount(100, 100, 100, date(2024, 3, 25), 20)
        self.assertEqual('Account Number: 100 Balance: $100.00\n'
                        'Minimum Balance: $20.00 Account Type: Savings'
                        , str(expected))
