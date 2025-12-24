"""Dunder Methods example"""

class Coordinates:
    def __init__(self, x: float, y: float) -> float:
        self.x = x
        self.y = y

    def __add__(self, other: object) -> "Coordinates":
        new_coordinate = Coordinates(self.x , self.y)
        new_coordinate.x = self.x + other.x
        new_coordinate.y = self.y + other.y
        return new_coordinate

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
if __name__ == '__main__':
    c1 = Coordinates(2, 3)
    c2 = Coordinates(4, 5)
    c3 = c1 + c2
    print(c3)