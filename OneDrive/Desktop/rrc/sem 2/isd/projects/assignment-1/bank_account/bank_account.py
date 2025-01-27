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

    @property
    def account_number(self) -> int:
        """
        Getter for the account_number attribute.

        Args:
            None

        Returns:
            int: The bank account number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Getter for the client_number attribute.

        Args:
            None

        Returns:
            int: The client number associated with the account.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Getter for the balance attribute.

        Args:
            None

        Returns:
            float: The current account balance.
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Updates the balance with a given amount.

        Args:
            amount (float): The amount to modify the balance by.

        Returns:
            None

        Raises:
            ValueError: If amount cannot be converted to a float.
        """
        try:
            self.__balance += float(amount)
        except ValueError as e:
            print(f"ERROR: {e}")
