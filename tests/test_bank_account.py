"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(200, 200, 200)
    
    def test_initialization_with_valid_args_sets_attributes(self):
        expected = BankAccount(200, 200, 200)

        self.assertEqual(200, expected._BankAccount__account_number)
        self.assertEqual(200, expected._BankAccount__client_number)
        self.assertEqual(200, expected._BankAccount__balance)

    def test_initialization_with_non_numeric_balance_sets_to_zero(self):
        expected = BankAccount(200, 200, "two hundred")

        self.assertEqual(0, expected._BankAccount__balance)

    def test_initialization_with_non_integer_account_number_raises_error(self):
        with self.assertRaises(ValueError):
            BankAccount("two hundred", 200, 200)

    def test_initialization_with_non_integer_client_number_raises_error(self):
        with self.assertRaises(ValueError):
            BankAccount(200, "two hundred", 200)

    def test_account_number_getter_returns_account_number_value(self):
        self.assertEqual(200, self.bank_account.account_number)

    def test_client_number_getter_returns_client_number_value(self):
        self.assertEqual(200, self.bank_account.client_number)

    def test_balance_getter_returns_balance_value(self):
        self.assertEqual(200, self.bank_account.balance)

    def test_balance_update_with_positive_amount(self):
        self.bank_account.update_balance(100)

        self.assertEqual(self.bank_account.balance, 300)

    def test_balance_update_with_negative_amount(self):
        self.bank_account.update_balance(-100)

        self.assertEqual(self.bank_account.balance, 100)

    def test_balance_update_with_non_numeric_amount_does_not_change_balance(self):
        self.bank_account.update_balance("hundred")

        self.assertEqual(self.bank_account.balance, 200)

    def test_deposit_with_valid_amount_updates_balance(self):
        self.bank_account.deposit(100)

        self.assertEqual(self.bank_account.balance, 300)

    def test_deposit_with_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100)

    def test_withdrawal_with_valid_amount_updates_balance(self):
        self.bank_account.withdraw(100)

        self.assertEqual(self.bank_account.balance, 100)

    def test_withdrawal_with_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100)

    def test_withdrawal_amount_exceeding_balance_raises_error(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(400)

    def test_string_representation_with_valid_data(self):
        expected = "Account Number: 200 Balance: $200.00\n"

        self.assertEqual(expected, str(self.bank_account))