"""
Description: Defines ServiceChargeStrategy class

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod


class ServiceChargeStrategy(ABC):
    """
    Strategy class for calculation of service charges for different accounts.

    """

    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Used in application of the strategy pattern to calculate
        service charges for different bank account types.

        Args:
            account (BankAccount): The account information of the bank account.
        
        Returns:
            float: The service charges of a bank account.

        """
        pass
            





