"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jashanpreet Singh Sidhu"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date, timedelta
from client.client import Client


# 2. Create a Client object with data of your choice.
instance1 = Client(20, 'Jashan', 'Sidhu', 'cholamola@gmail.com')


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
instance2 = ChequingAccount(100, 20, 10000, date(2012, 9, 20), -20, 0.10)
instance3 = SavingsAccount(100, 20, 1000000, date(2014, 10, 1), 5)


# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
instance2.attach(instance1)
instance3.attach(instance1)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(30, 'Raahil', 'cholamola', 'cholamola@outlook.com')
instance4 = SavingsAccount(200, 30, 20000, date(2016, 8, 12), 4)
instance4.attach(client2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

try:
    instance2.deposit(500)
    instance2.withdraw(300)
    instance2.withdraw(20000)
except ValueError as e:
    print(f"Error with ChequingAccount transaction: {e}")

try:
    instance3.deposit(10000)
    instance3.withdraw(500000)
    instance3.withdraw(5000)
except ValueError as e:
    print(f"Error with SavingsAccount transaction: {e}")

try:
    instance4.deposit(20000)
    instance4.withdraw(15000)
    instance4.withdraw(30000)
except ValueError as e:
    print(f"Error with SavingsAccount transaction: {e}")