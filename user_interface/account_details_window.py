__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
from copy import deepcopy
from bank_account import *
from PySide6.QtCore import Slot

class AccountDetailsWindow(DetailsWindow):
 # Define custom signal
    balance_updated = Signal(object)  # Will emit BankAccount object
    
    def __init__(self, account):
        super().__init__()
        
        # Validate account
        if not isinstance(account, (ChequingAccount, SavingsAccount, InvestmentAccount)):
            self.reject()
            return
        
        # Store account (make a copy to prevent direct modification)
        self.account = deepcopy(account)
        
        # Display account info
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:,.2f}")
        
        # Connect signals
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)
    
    @Slot()
    def on_apply_transaction(self):
        """Handle deposit/withdraw button clicks"""
        # Get and validate amount
        try:
            amount = float(self.transaction_amount_edit.text())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Amount",
                "Please enter a valid positive number.",
                QMessageBox.Ok
            )
            self.transaction_amount_edit.setFocus()
            return
        
        # Determine transaction type
        sender = self.sender()
        transaction_type = "Deposit" if sender == self.deposit_button else "Withdraw"
        
        try:
            # Perform transaction
            if transaction_type == "Deposit":
                self.account.deposit(amount)
            else:
                self.account.withdraw(amount)
            
            # Update display
            self.balance_label.setText(f"${self.account.balance:,.2f}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            
            # Emit signal with updated account
            self.balance_updated.emit(self.account)
            
        except Exception as e:
            QMessageBox.warning(
                self,
                f"{transaction_type} Failed",
                f"{transaction_type} failed: {str(e)}",
                QMessageBox.Ok
            )
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
    
    @Slot()
    def on_exit(self):
        """Close the window"""
        self.close()