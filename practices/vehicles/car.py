from vehiclewithengine import VehicleWithEngine

class Car(VehicleWithEngine):
    def __init__(self, brand: str, model: str, fuel: str, doors_number: int) -> None:
        super().__init__(brand, model, fuel)
        self.doors_number = doors_number

    def details(self) -> None:
        print(f'Name: {self.model}\nBrand: {self.brand}\nFuel type: {self.fuel}\nDoors Number: {self.doors_number}')