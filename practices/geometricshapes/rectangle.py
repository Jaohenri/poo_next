from geometric_shape import GeometricShape

class Rectangle(GeometricShape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError('Width and Height cannot have values less than 0')
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.height * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def details(self):
        return f"Rectangle - Width: {self.width}, Height: {self.height}"