"""
Instrument representation

This module defines the Piano class, which represents a piano
instrument and implements the play behavior.
"""
from instrument import Instrument

class Piano(Instrument):
    """
    Represents a Piano
    """
    def play(self) -> None:
        """
        Plays the Drum
        """
        print('Playing piano.')
