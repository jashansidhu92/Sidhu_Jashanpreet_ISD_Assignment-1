"""
Description: Defines ManagementFeeStrategy class
which calculates charges for managing an investment 
account.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Used in calculation of Management Fee for investment accounts

    """

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, manegement_fee: float) -> None:
        """
        Initializes the class attributes.

        Args:
            date_created (date): Account creation date.
            management_fee (float): The basic management fee for investment accounts.

        """

        self.__management_fee = manegement_fee
        self.__date_created = date_created
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Used in calculation of service charges for investment accounts.

        Args:
            account (BankAccount): Bank Account details.
        
        Returns:
            float: The service charges for investment accounts.

        """

        if self.__date_created < ManagementFeeStrategy.TEN_YEARS_AGO:  
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE 
                            + self.__management_fee)

        return service_charge
