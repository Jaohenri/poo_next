from geometric_shape import GeometricShape

class Circle(GeometricShape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('Radius cannot have a value lower than 0')
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * (self.radius**2)
    
    def calculate_perimeter(self) -> float:
        return 2 * 3.14 * self.radius
    
    def details(self) -> str:
        return f"Circle - Radius: {self.radius}"
    