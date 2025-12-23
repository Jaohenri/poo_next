"""Module for Circle"""
from geometric_shape import GeometricShape

class Circle(GeometricShape):
    """
    Represents a Circle
    
    Methods:
    calculate_area -> Float: Calculate the Area of the circle.
    calculate_perimeter -> float: Calculate the perimeter of the circe.
    details -> str: returns the circle details.
    """
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('Radius cannot have a value lower than 0')
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Calculate the Area of the circle.
        """
        return 3.14 * (self.radius**2)

    def calculate_perimeter(self) -> float:
        """
        Calculate the Perimeter of the circle.
        """
        return 2 * 3.14 * self.radius

    def details(self) -> str:
        """
        Returns details of the circle.
        """
        return f"Circle - Radius: {self.radius}"
    