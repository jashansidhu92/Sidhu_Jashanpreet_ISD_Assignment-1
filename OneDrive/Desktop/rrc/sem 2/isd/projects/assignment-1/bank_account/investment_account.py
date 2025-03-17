"""
Description: A file that defines the BankAccount class for 
managing bank account records for investment accounts.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.1.0"


from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    Manages investment accounts.
    
    """
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float
                 , date_created: date, management_fee: float) -> None:
        """
        Initializes the class attributes.

        Args:
            account_number (int): The bank account number as an integer.
            client_number (int): The client number associated with the account holder.
            balance (float): The initial balance of the account.
            date_created(date): The date on which the bank account was created.
            management_fee(float): flat rate which bank charges for investment accounts

        Returns:
            None

        Raises:
            ValueError: If account_number or client_number are not integers, or if balance is not a valid float.

        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            management_fee = float(management_fee)
            self.__management_fee = management_fee
        except:
            self.__management_fee = 2.55

        self.__management_fee_strategy = ManagementFeeStrategy(self._date_created, self.__management_fee)

    def __str__(self) -> str:
        """
        Returns a string representation of investment account details.

        Args:
            None

        Returns:
            str: String representation of investment account details.
        
        """
        if self._date_created >= InvestmentAccount.TEN_YEARS_AGO:
            return (super().__str__()
                    + f'Date Created: {self._date_created} '
                    + f'Management Fee: ${self._InvestmentAccount__management_fee:,.2f} '
                    + f'Account Type: Investment')
            
    
        else:
            return (super().__str__()
                    + f'Date Created: {self._date_created} '
                    + f'Management Fee: Waived '
                    + f'Account Type: Investment')
        
    def get_service_charges(self) -> float:
        """
        Calculates the service charge for investment accounts.

        Args:
            None

        Returns:
            service_charge(float): The service charges for bank's investment accounts.
        
        """

        service_charge = self.__management_fee_strategy.calculate_service_charges(self)
        return service_charge
        


        