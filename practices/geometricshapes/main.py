"""
Example usage of Rectangle and Circle classes.
"""
from rectangle import Rectangle
from circle import Circle

if __name__ == '__main__':
    forms = [
        Rectangle(7, 5),
        Rectangle(8, 1),
        Rectangle(13, 10),
        Circle(10),
        Circle(5.5),
        Circle(50)
    ]

    for form in forms:
        print(form.details())
        print(f'Area: {form.calculate_area():.2f}')
        print(f'Perimeter: {form.calculate_perimeter():.2f}\n')
