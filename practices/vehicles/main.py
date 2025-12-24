"""
Demonstrates the usage of vehicle classes.

This script creates different types of vehicles and
executes their behaviors, such as moving and displaying details.
"""
from car import Car
from vehiclewithoutengine import VehicleWithoutEngine
from vehiclewithengine import VehicleWithEngine

if __name__ == '__main__':

    byd_dolphin = Car('Byd', 'Byd Dolphin', 'Eletricity', 4)
    bicycle = VehicleWithoutEngine('Canyon', 'Aeroad CFR AXS', 'Pedals - Human Propulsion')
    motorcycle = VehicleWithEngine('Yamaha', 'FZ15 FLEX', 'Fuel and Alcohol')

    byd_dolphin.move()
    byd_dolphin.details()

    print('\n-----------------------------\n')

    bicycle.move()

    motorcycle.move()
