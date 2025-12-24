"""
Base vehicle implementation.

This module defines the vehicle class.
"""
class Vehicle:
    """
    Represents a vehicle.
    """
    def __init__(self, brand: str, model: str) -> None:
        """
        Initializes a vehicle instance.

        Args:
            brand: Vehicle brand.
            model: Vehicle model.
        """
        self.brand = brand
        self.model = model

    def move(self) -> None:
        """Displays a message that the vehicle is moving"""
        print(f'The {self.model} from {self.brand} is moving\n')
