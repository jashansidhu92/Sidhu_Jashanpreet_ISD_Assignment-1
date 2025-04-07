"""
Description: Defines OverdraftStrategy class
which calculates charges for overdrafts.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculation of service charges for overdrafts.

    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float) -> None:
        """
        Used for initializing the class attributes.

        Args:
            overdraft_limit (float): The limit below which overdraft
                charges are applied.
            overdraft_rate (float): The rate at which the charges are applied
                to overdrafts.

        Returns:
            None

        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The strategy function for calculating charges for overdrafts.

        Args:
            account (BankAccount): The account details of the bank account.
        
        Returns:
            float: The service charges for a chequing account.

        """

        if account.balance >= self.__overdraft_limit:
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE

        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE + 
                            (self.__overdraft_limit - account.balance) * 
                            self.__overdraft_rate)  
                 
        return service_charge
        