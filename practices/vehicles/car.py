from vehiclewithengine import VehicleWithEngine

class Car(VehicleWithEngine):
    def __init__(self, brand, model, fuel, doors_number):
        super().__init__(brand, model, fuel)
        self.doors_number = doors_number

    def details(self):
        print(f'Name: {self.model}\nBrand: {self.brand}\nFuel type: {self.fuel}\nDoors Number: {self.doors_number}')