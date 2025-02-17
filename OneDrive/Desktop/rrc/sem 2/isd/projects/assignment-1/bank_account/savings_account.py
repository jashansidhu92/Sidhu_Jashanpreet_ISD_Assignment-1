"""
Description: File which defines the 
SavingsAccount class which is used to manage bank
account records for saving accounts.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Used to manage savings accounts for clients.

    """
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, account_number: int, client_number: int, balance: float,
                date_created: date, minimum_balance: float) -> None:
        """
        Initializer for the class attributes for SavingsAccount class.

        Args:
            account_number (int): An integer value representing the bank account number.
            client_number (int): An integer value representing the client number representing
                                  the account holder.
            balance (float): A float value representing the current balance of the bank account.
            date_created(date): The date when the bank account was created.
            minimum_balance(float): A minimum value a balance can be before further
                                    service charges apply.

        Returns:
            None

        Raises:
            ValueError: When account_number and client_number do not classify as integers.
            ValueError: When the balance cannot be converted to a float.
        
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            minimum_balance = float(minimum_balance)
            self.__minimum_balance = minimum_balance
        except:
            self.__minimum_balance = 50

    def __str__(self) -> str:
        """
        Returns a string representation of the details of a savings account.

        Args:
            None

        Returns:
            str: A formatted string representing the information of a savings
                account.
        
        """
        return (super().__str__()
            + f'Minimum Balance: ${self.__minimum_balance:,.2f} '
            + f'Account Type: Savings')
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge for a savings account.

        Args:
            None

        Returns:
            service_charge(float): The service charge for a savings account.
        
        """
        if self._BankAccount__balance >= self.__minimum_balance:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        else:
            service_charge = BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

        return service_charge


        