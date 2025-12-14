from vehicle import Vehicle

class VehicleWithEngine(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.fuel = fuel
    
    def moviment(self):
        print(f'The {self.model} from {self.brand} is moving with {self.fuel}.\n')