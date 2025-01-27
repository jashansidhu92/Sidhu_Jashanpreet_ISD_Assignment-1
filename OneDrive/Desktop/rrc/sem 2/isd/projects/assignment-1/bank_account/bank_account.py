"""
Description: A file that defines the BankAccount class for managing bank account records.
"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"



class BankAccount:
    """
    The BankAccount class: Used to manage and store bank account information.
    """

    def __init__(self, account_number: int, client_number: int, balance: float = None) -> None:
        """
        Initializes the class attributes.

        Args:
            account_number (int): The bank account number as an integer.
            client_number (int): The client number associated with the account holder.
            balance (float): The initial balance of the account.

        Returns:
            None

        Raises:
            ValueError: If account_number or client_number are not integers, or if balance is not a valid float.
            
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")

        try:
            self.__balance = float(balance) if balance is not None else 0.0
        except ValueError:
            self.__balance = 0.0