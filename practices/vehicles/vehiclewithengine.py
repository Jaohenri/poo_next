"""
Vehicle with engine implementation.

This module defines the VehicleWithEngine class.
"""
from vehicle import Vehicle

class VehicleWithEngine(Vehicle):
    """
    Represents a vehicle with an engine
    """
    def __init__(self, brand: str, model: str, fuel: str) -> None:
        """
        Initializes a vehicle with an engine instance.

        Args:
            brand: Vehicle brand.
            model: Vehicle model.
            fuel: Fuel type used by the vehicle.
        """
        super().__init__(brand, model)
        self.fuel = fuel

    def move(self) -> None:
        """Displays a message that the vehicle is moving"""
        print(f'The {self.model} from {self.brand} is moving with {self.fuel}.\n')
