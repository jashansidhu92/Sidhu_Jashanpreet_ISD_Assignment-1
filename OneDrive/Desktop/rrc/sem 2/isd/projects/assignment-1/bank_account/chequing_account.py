"""
Description: A file that defines the BankAccount class for 
managing bank account records for chequing accounts.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from datetime import date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    Manages chequing accounts.
    
    """

    def __init__(self, account_number: int, client_number:int, balance: float
                , date_created: date, overdraft_limit: float, overdraft_rate: float) -> None:
        """
        Initializes the class attributes.

        Args:
            account_number (int): The bank account number as an integer.
            client_number (int): The client number associated with the account holder.
            balance (float): The initial balance of the account.
            date_created(date): The date on which the bank account was created.
            overdraft_limit(float): The maximum amount a balance can be overdrawn(below 0.00)
            before overdraft fees are applied.
            overdraft_rate(float): The rate to which overdraft fees will be applied.

        Returns:
            None

        Raises:
            ValueError: If account_number or client_number are not integers, or if balance is not a valid float.
                   
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            overdraft_limit = float(overdraft_limit)
            self.__overdraft_limit = overdraft_limit
        except:
            self.__overdraft_limit = -100

        try:
            overdraft_rate = float(overdraft_rate)
            self.__overdraft_rate = overdraft_rate
        except:
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        """
        String representation for the details of an account.
        
        Args:
            None

        Returns:
            str: String representation of account information.

        """
        return (super().__str__()
                + f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                + f"Overdraft Rate: {self.__overdraft_rate * 100:,.0f}% "
                + f"Account Type: Chequing")
    
    def get_service_charges(self) -> float:
        """
        Calculates service charge for chequing accounts.

        Args:
            None

        Returns:
            service_charge(float): The service charge for a chequing account.
        
        """
        if self._BankAccount__balance >= self.__overdraft_limit:
            service_charge = BankAccount.BASE_SERVICE_CHARGE

        else:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE + 
                            (self.__overdraft_limit - self._BankAccount__balance) *
                            self.__overdraft_rate)
            
        return service_charge
