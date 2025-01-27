"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

from client.client import Client
import unittest

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1, "Jashan", "Cholamola", "sidhu@academic.rrc.ca")
    
    def test_init_with_valid_inputs_sets_attributes(self):
        expected = Client(1, "Jashan", "Cholamola", "sidhu@academic.rrc.ca")

        self.assertEqual(1, expected._Client__client_number)
        self.assertEqual("Jashan", expected._Client__first_name)
        self.assertEqual("Cholamola", expected._Client__last_name)
        self.assertEqual("sidhu@academic.rrc.ca", expected._Client__email_address)

    def test_init_with_invalid_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client("one", "Jashan", "Cholamola", "sidhu@academic.rrc.ca")

    def test_init_with_blank_first_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(1," ","Cholamola","sidhu@academic.rrc.ca")

    def test_init_with_blank_last_name_raises_valueerror(self):
        with self.assertRaises(ValueError):
            Client(1, "Jashan", " ", "sidhu@academic.rrc.ca")

    def test_init_with_invalid_email_address_sets_default_value(self):
        expected = Client(1,"Jashan", "Cholamola", "sidhuacademic.rrc.ca")

        self.assertEqual("email@pixell-river.com", expected._Client__email_address)

    def test_client_number_getter_returns_client_number(self):
        self.assertEqual(1, self.client.client_number)

    def test_first_name_getter_returns_first_name(self):
        self.assertEqual("Jashan", self.client.first_name)

    def test_last_name_getter_returns_last_name(self):
        self.assertEqual("Cholamola", self.client.last_name)

    def test_email_address_accessor_returns_email_address(self):
        self.assertEqual("sidhu@academic.rrc.ca", self.client.email_address)

    def test_str_with_valid_inputs_returns_proper_string_format(self):
        expected = ("Cholamola, Jashan [1] - sidhu@academic.rrc.ca\n")
        
        self.assertEqual(expected, str(self.client))
