"""
Module for Rectangle
"""
from geometric_shape import GeometricShape

class Rectangle(GeometricShape):
    """
    Represents a Rectangle
    
    Methods:
    calculate_area -> Float: Calculate the Area of the rectangle.
    calculate_perimeter -> float: Calculate the perimeter of the rectangle.
    details -> str: returns the rectangle details.
    """
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError('Width and Height cannot have values less than 0')
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the Area of the rectangle.
        """
        return self.height * self.width

    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def details(self) -> str:
        """
        Returns details of the rectangle.
        """
        return f"Rectangle - Width: {self.width}, Height: {self.height}"
