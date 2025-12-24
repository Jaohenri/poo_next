"""
Car implementation.

This module defines the Car class, a vehicle with an engine
that includes a specific number of doors.
"""
from vehiclewithengine import VehicleWithEngine

class Car(VehicleWithEngine):
    """Represents a car vehicle."""
    def __init__(self, brand: str, model: str, fuel: str, doors_number: int) -> None:
        """
        Initializes a car instance.

        Args:
            brand: Vehicle brand.
            model: Vehicle model.
            fuel: Fuel type used by the car.
            doors_number: Number of doors of the car.
        """
        super().__init__(brand, model, fuel)
        self.doors_number = doors_number

    def details(self) -> None:
        """Displays the details of the car."""
        print(
            f'Name: {self.model}\n'
            f'Brand: {self.brand}\n'
            f'Fuel type: {self.fuel}\n'
            f'Doors Number: {self.doors_number}')
