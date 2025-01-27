"""
Description: A file that contains the 
Client class responsible for managing client data.

"""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """
    Client class: Handles the management of client information.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str) -> None:
        """
        Initializes the class attributes.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Returns:
            None

        Raises:
            ValueError: If client_number is not an integer, or if first_name or last_name are empty.
            EmailNotValidError: If email_address is not formatted correctly.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")

        if first_name.strip():
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be empty.")

        if last_name.strip():
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be empty.")

        try:
            valid_email = validate_email(email_address)
            self.__email_address = valid_email.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Getter for the client_number attribute.

        Args:
            None

        Returns:
            int: The unique identifier of the client.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Getter for the first_name attribute.

        Args:
            None

        Returns:
            str: The first name of the client.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Getter for the last_name attribute.

        Args:
            None

        Returns:
            str: The last name of the client.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Getter for the email_address attribute.

        Args:
            None

        Returns:
            str: The email address of the client.
        """
        return self.__email_address

