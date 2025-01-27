"""
Description: A client program designed to verify the functionality 
of the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jashanpreet Singh Sidhu"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the methods and functionality of BankAccount and Client classes."""
    # Ensure that exceptions are caught and displayed during execution.

    # 1. Create a valid instance of the Client class.
    # Use unique valid values for the inputs.
    try:
        client_instance = Client(100,"Jashan", "Cholamola", "sidhu@academic.rrc.ca")
    except ValueError as e:
        print("error:", e)
    
    # 2. Declare a BankAccount object with initial None values.
    try:
        bank_account_instance = BankAccount(None, None, None)
    except ValueError as e:
        print("error:", e)    

    # 3. Create a valid BankAccount object.
    # Use an integer for the account number, 
    # the client_number from the Client instance created earlier, 
    # and a float for the balance.
    try:
        valid_bank_account_instance = BankAccount(100, client_instance.client_number, 300.00)
    except ValueError as e:
        print("ERROR:", e)
    
    # 4. Attempt to create a BankAccount instance with an invalid balance type.
    try:
        invalid_bank_account_instance = BankAccount(100, client_instance.client_number, "ten")
    except ValueError as e:
        print("ERROR:", e)
    
    # 5. Print the Client and BankAccount instances created above.
    print(str(client_instance))
    print(str(valid_bank_account_instance))

    # 6. Attempt to deposit a non-numeric value into the BankAccount.
    try:
        valid_bank_account_instance.deposit("hundred")
    except ValueError as e:
        print("error:", e)

    # 7. Attempt to deposit a negative value into the BankAccount.
    try:
        valid_bank_account_instance.deposit(-200)
    except ValueError as e:
        print("error:", e)
    
    # 8. Attempt to withdraw a valid amount from the BankAccount.
    try:
        valid_bank_account_instance.withdraw(50)
    except ValueError as e:
        print("error:", e)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount.
    try:
        valid_bank_account_instance.withdraw("hundred")
    except ValueError as e:
        print("error:", e)

    # 10. Attempt to withdraw a negative value from the BankAccount.
    try:
        valid_bank_account_instance.withdraw(-50)
    except ValueError as e:
        print("error:", e)

    # 11. Attempt to withdraw an amount exceeding the current balance.
    try:
        valid_bank_account_instance.withdraw(2000)
    except ValueError as e:
        print("error:", e)

    # 12. Print the BankAccount instance after all operations.
    print(str(valid_bank_account_instance))


if __name__ == "__main__":
    main()