class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def moviment(self):
        print(f'The {self.model} from {self.brand} is moving\n')

class VehicleWithoutEngine(Vehicle):
    def __init__(self, brand, model, propulsion_type):
        super().__init__(brand, model)
        self.propulsion_type = propulsion_type

    def moviment(self):
        print(f'The {self.model} from {self.brand} is moving.',
              f'But, as this vehicle dont have an engine, is moving by {self.propulsion_type}\n')

class VehicleWithEngine(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.fuel = fuel
    
    def moviment(self):
        print(f'The {self.model} from {self.brand} is moving with {self.fuel}.\n')

class Car(VehicleWithEngine):
    def __init__(self, brand, model, fuel, doors_number):
        super().__init__(brand, model, fuel)
        self.doors_number = doors_number

    def details(self):
        print(f'Name: {self.model}\nBrand: {self.brand}\nFuel type: {self.fuel}\nDoors Number: {self.doors_number}')

if __name__ == '__main__':
    byd_dolphin = Car('Byd', 'Byd Dolphin', 'Eletricity', 4)
    bicycle = VehicleWithoutEngine('Canyon', 'Aeroad CFR AXS', 'Pedals - Human Propulsion')

    byd_dolphin.moviment()
    byd_dolphin.details()
    print('\n-----------------------------\n')
    bicycle.moviment()