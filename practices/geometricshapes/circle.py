from geometric_shape import GeometricShape

class Circle(GeometricShape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Radius cannot have a value lower than 0')
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius**2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
    def details(self):
        return f"Circle - Radius: {self.radius}"
    