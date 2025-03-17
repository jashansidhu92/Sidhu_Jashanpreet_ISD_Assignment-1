"""This module defines the Subject class for the Observer pattern."""

__author__ = "Jashanpreet Singh Sidhu"
__version__ = "1.0.0"

from abc import ABC,abstractmethod
from observer import Observer

class Subject(ABC):
    """
    Subject class: Maintains Subject data.Is abstract class
    
    """

    def __init__(self) -> None:
        """
        Initializes an empty list of observers.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attaches an observer to the subject.

        Args:
            observer (Observer): The observer to be added.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detaches an observer from the subject.

        Args:
            observer (Observer): The observer to be removed.
        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Notifies all attached observers with a message.

        Args:
            message (str): The message to be sent to observers.
        """
        pass
