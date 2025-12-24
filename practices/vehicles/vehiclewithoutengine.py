"""
Vehicle without engine implementation.

This module defines the VehicleWithoutEngine class.
"""
from vehicle import Vehicle

class VehicleWithoutEngine(Vehicle):
    """
    Represents a vehicle without an engine
    """
    def __init__(self, brand: str, model: str, propulsion_type: str) -> None:
        """
        Initializes a vehicle without an engine instance.

        Args:
            brand: Vehicle brand.
            model: Vehicle model.
            propulsion_type: propulsion type used by the vehicle.
        """
        super().__init__(brand, model)
        self.propulsion_type = propulsion_type

    def move(self) -> None:
        """Displays a message that the vehicle is moving"""
        print(f'The {self.model} from {self.brand} is moving.',
              f'But, as this vehicle dont have an engine, is moving by {self.propulsion_type}\n')
        