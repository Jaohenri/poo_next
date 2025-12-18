from vehicle import Vehicle

class VehicleWithoutEngine(Vehicle):
    def __init__(self, brand: str, model: str, propulsion_type: str) -> None:
        super().__init__(brand, model)
        self.propulsion_type = propulsion_type

    def moviment(self) -> None:
        print(f'The {self.model} from {self.brand} is moving.',
              f'But, as this vehicle dont have an engine, is moving by {self.propulsion_type}\n')