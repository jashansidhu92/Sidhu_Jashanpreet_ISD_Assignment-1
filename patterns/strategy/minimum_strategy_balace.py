"""
Description: Defines MinimumBalanceStrategy class
which calculates service charges for savings accounts.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Used in calculation of service charges for savings accounts.

    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float) -> None:
        """
        Initializes the class attributes.

        Args:
            minimum_balance (float): The balance below which the premium 
                charges are added.

        Returns:
            None
        
        """

        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Used in calculation of service charges for savings account.

        Args:
            account (BankAccount): Bank Account details.
        
        Returns:
            float: The service charge for savings account.
        
        """

        if account.balance >= self.__minimum_balance:

            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        
        else:

            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM)

        return service_charge