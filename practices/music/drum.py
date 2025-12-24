"""
Instrument representation

This module defines the Drum class, which represents a drum
instrument and implements the play behavior.
"""
from instrument import Instrument

class Drum(Instrument):
    """
    Represents a Drum
    """
    def play(self) -> None:
        """
        Plays the Drum
        """
        print('Playing drums.')
        