"""
Base definition for Instruments
"""
class Instrument:
    """
    Represents a instrument

    Defines a common interface for instruments.
    """
    def play(self) -> None:
        """
        Plays the instrument
        """
        print('Playing an instrument.')
