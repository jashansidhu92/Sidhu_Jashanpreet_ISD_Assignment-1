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
    
    
        
