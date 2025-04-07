"""
Description: Unit tests for the ChequingAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py

"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def test_init_correct_arguments_attributes_are_set(self):
        expected = ChequingAccount(2000, 2000, 2000, date(2015, 1, 1), -20, 0.06)
        self.assertEqual(2000, expected._BankAccount__account_number)
        self.assertEqual(2000, expected._BankAccount__client_number)
        self.assertEqual(2000, expected._BankAccount__balance)
        self.assertEqual(date(2015, 1, 1), expected._date_created)
        self.assertEqual(-20, expected._ChequingAccount__overdraft_limit)
        self.assertEqual(0.06, expected._ChequingAccount__overdraft_rate)

    def test_invalid_overdraft_limit_type_sets_to_default_value(self):
        expected = ChequingAccount(2000, 2000, 2000, date(2015, 1, 1), 'twenty', 0.06)
        self.assertEqual(-100, expected._ChequingAccount__overdraft_limit)

    def test_invalid_overdraft_rate_type_sets_to_default_value(self):
        expected = ChequingAccount(2000, 2000, 2000, date(2015, 1, 1), -20, '6%')
        self.assertEqual(0.05, expected._ChequingAccount__overdraft_rate)

    def test_invalid_date_created_sets_to_today(self):
        expected = ChequingAccount(100, 100, 100, "(1/1/15)", -10, 0.08)
        self.assertEqual(date(2025, 3, 16), expected._date_created)

    def test_get_service_charges_balance_greater_than_limit_sets_charges_to_default(self):
        expected = ChequingAccount(2000, 2000, 2000, date(2015, 1, 1), -20, 0.06)
        self.assertEqual(0.50, expected.get_service_charges())

    def test_get_service_charges_balance_smaller_than_limit_calculates_service_charge(self):
        expected = ChequingAccount(2000, 2000, -2000, date(2015, 1, 1), -20, 0.06)
        self.assertEqual(119.30, expected.get_service_charges())

    def test_get_service_charges_balance_equal_to_limit_sets_charges_to_default(self):
        expected = ChequingAccount(2000, 2000, -20, date(2015, 1, 1), -20, 0.06)
        self.assertEqual(0.50, expected.get_service_charges())

    def test_str_valid_inputs_returns_formatted_string(self):
        expected = ChequingAccount(2000, 2000, 2000, date(2015, 1, 1), -20, 0.06)
        self.assertEqual("Account Number: 2000 Balance: $2,000.00\nOverdraft " 
                        "Limit: $-20.00 Overdraft Rate: 6% Account Type: Chequing"
                        , str(expected))

        