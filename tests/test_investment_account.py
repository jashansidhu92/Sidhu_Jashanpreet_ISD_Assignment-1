"""
Description: Unit tests for the InvestmentAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py

"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date

class TestInvestmentAccount(unittest.TestCase):

    def test_init_valid_inputs_attributes_are_set(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2015, 1, 1), 10)
        self.assertEqual(2000, expected._BankAccount__account_number)
        self.assertEqual(2000, expected._BankAccount__client_number)
        self.assertEqual(2000, expected._BankAccount__balance)
        self.assertEqual(date(2015, 1, 1), expected._date_created)
        self.assertEqual(10, expected._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_sets_to_default_value(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2015, 1, 1), 'ten')
        self.assertEqual(2.55, expected._InvestmentAccount__management_fee)

    def test_get_service_charges_date_created_more_than_10_years_ago_waived_fee(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2010, 1, 1), 10)
        self.assertEqual(0.50, expected.get_service_charges())

    def test_get_service_charges_date_created_exactly_10_years_ago_calculates_charges(self):
        expected = InvestmentAccount(2000, 2000, 2000, InvestmentAccount.TEN_YEARS_AGO, 10)
        self.assertEqual(10.50, expected.get_service_charges())

    def test_get_service_charges_date_created_within_10_years_calculates_charges(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2015, 1, 1), 10)
        self.assertEqual(0.5, expected.get_service_charges())

    def test_str_date_created_more_than_ten_years_ago_returns_string(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2010, 1, 1), 10)
        self.assertEqual("Account Number: 2000 Balance: $2,000.00\nDate Created: "
                         "2010-01-01 Management Fee: Waived Account Type: "
                         "Investment", str(expected))
        
    def test_str_date_created_less_than_ten_years_ago_returns_string(self):
        expected = InvestmentAccount(2000, 2000, 2000, date(2015, 1, 1), 10)
        self.assertEqual("Account Number: 2000 Balance: $2,000.00\nDate Created: "
                         "2015-01-01 Management Fee: Waived Account Type: "
                         "Investment", str(expected))