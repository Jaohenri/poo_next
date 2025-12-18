from geometric_shape import GeometricShape

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError('Width and Height cannot have values less than 0')
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.height * self.width
    
    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def details(self) -> str:
        return f"Rectangle - Width: {self.width}, Height: {self.height}"