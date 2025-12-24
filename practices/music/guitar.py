"""
Instrument representation

This module defines the Guitar class, which represents a Guitar
instrument and implements the play behavior.
"""
from instrument import Instrument

class Guitar(Instrument):
    """
    Represents a Guitar
    """
    def play(self) -> None:
        """
        Plays the Guitar
        """
        print('Playing guitar.')
    