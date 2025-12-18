class Vehicle:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def moviment(self) -> None:
        print(f'The {self.model} from {self.brand} is moving\n')







