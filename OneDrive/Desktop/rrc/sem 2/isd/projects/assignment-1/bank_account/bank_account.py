"""
Description: A file that defines the BankAccount class for managing bank account records.
"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "2.0.0"

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """
    The BankAccount class: Used to manage and store bank account information.

    """
    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date) -> None:
        """
        Initializes the class attributes.

        Args:
            account_number (int): The bank account number as an integer.
            client_number (int): The client number associated with the account holder.
            balance (float): The initial balance of the account.
            date_created(date): The date on which the bank account was created.

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
        
        if isinstance(date_created, date):
            self._date_created = date_created

        else:
            self._date_created = date.today()

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

    def deposit(self, amount: float) -> None:
        """
        Deposits a given amount into the account.

        Args:
            amount (float): The deposit amount.

        Returns:
            None

        Raises:
            ValueError: If the amount is not a positive float or is non-numeric.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount must be numeric: {amount}.")

        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive: ${amount:,.2f}.")
        
        self.update_balance(amount)


    def withdraw(self, amount: float) -> None:
        """
        Withdraws a given amount from the account.

        Args:
            amount (float): The withdrawal amount.

        Returns:
            None

        Raises:
            ValueError: If the amount is not numeric, not positive, or exceeds the current balance.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount must be numeric: {amount}.")

        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive: ${amount:,.2f}.")

        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount exceeds balance: ${amount:,.2f} (balance: ${self.__balance:,.2f}).")

        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        String representation of the bank account details.

        Args:
            None

        Returns:
            str: The formatted string showing account number and balance.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculates the service charges for accounts.

        Args:
            None
        
        Returns:
            float: The service charge for different accounts.

        """
        pass
