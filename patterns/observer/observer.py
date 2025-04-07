"""This module defines the Observer pattern class."""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.1.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer class: Maintains Observer data.Is abstract class
    
    """
    @abstractmethod
    def update(self, message: str) -> None:
        """
        Abstract method that handles an update message sent to the observer.
        Must be implemented in subclasses.

        Args:
            message (str): The message containing update information.

        """
        pass