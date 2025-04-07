__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Jashan Sidhu"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from bank_account.bank_account import BankAccount
from PySide6.QtCore import Qt, Slot, Signal
from ui_superclasses.lookup_window import LookupWindow
from user_interface.manage_data import load_data, update_data
from user_interface.account_details_window import AccountDetailsWindow

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()
        
        # Load data
        self.client_listing, self.accounts = load_data()
        
        # Connect signals
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)
    
    def on_lookup_client(self):
        """Handle lookup button click event"""
        # Get and validate client number
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Client Number",
                "Client number must be numeric.",
                QMessageBox.Ok
            )
            self.reset_display()
            return
        
        # Check if client exists
        if client_number not in self.client_listing:
            QMessageBox.warning(
                self,
                "Client Not Found",
                f"Client {client_number} does not exist.",
                QMessageBox.Ok
            )
            self.reset_display()
            return
        
        # Display client info
        client = self.client_listing[client_number]
        self.client_info_label.setText(
            f"{client.last_name}, {client.first_name} [{client.client_number}]"
        )
        
        # Populate account table
        self.account_table.setRowCount(0)  # Clear existing rows
        
        row = 0
        for account in self.accounts.values():
            if account.client_number == client_number:
                self.account_table.insertRow(row)
                
                # Account Number
                acc_num_item = QTableWidgetItem(str(account.account_number))
                acc_num_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                
                # Balance
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                
                # Date Created
                date_item = QTableWidgetItem(account.date_created)
                date_item.setTextAlignment(Qt.AlignCenter)
                
                # Account Type
                type_item = QTableWidgetItem(account.__class__.__name__)
                type_item.setTextAlignment(Qt.AlignCenter)
                
                # Add items to table
                self.account_table.setItem(row, 0, acc_num_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_item)
                self.account_table.setItem(row, 3, type_item)
                
                row += 1
        
        self.account_table.resizeColumnsToContents()
    
    @Slot()
    def on_text_changed(self):
        """Clear account table when client number changes"""
        self.account_table.setRowCount(0)
    
    @Slot(int, int)
    def on_select_account(self, row, column):
        """Handle account selection from table"""
        account_number_item = self.account_table.item(row, 0)
        
        if not account_number_item:
            QMessageBox.warning(
                self,
                "Invalid Selection",
                "Please select a valid account.",
                QMessageBox.Ok
            )
            return
        
        account_number = int(account_number_item.text())
        
        if account_number not in self.accounts:
            QMessageBox.warning(
                self,
                "Account Not Found",
                "Selected account does not exist.",
                QMessageBox.Ok
            )
            return
        
        # Open account details window
        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)
        details_window.balance_updated.connect(self.update_data)
        details_window.exec_()
    
    @Slot(object)
    def update_data(self, account):
        """Update account data when balance changes"""
        # Update table
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)
            if item and int(item.text()) == account.account_number:
                # Update balance display
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)
                break
        
        # Update accounts dictionary
        self.accounts[account.account_number] = account
        
        # Update CSV file
        update_data(account)

    
        
