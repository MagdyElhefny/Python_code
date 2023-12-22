# Solid principle


# 1->>> S = Single responsibility principle


# Before applying SRP
class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):
        # logic to generate report
        pass

    def save_to_file(self):
        # logic to save report to a file
        pass

# After applying SRP
class Report:
    def __init__(self, content):
        self.content = content

    def generate_report(self):

        pass

class ReportSaver:
    @staticmethod
    def save_to_file(report):

        pass


# 2->>>o = open close


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    @staticmethod
    def calculate_area(rectangle):
        return rectangle.width * rectangle.height


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# 3->>> l = Liskov Substitution Principle (LSP):

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def print_area(shape):
    print(f"Area: {shape.area()}")


rectangle = Rectangle(3, 4)
square = Square(5)

print_area(rectangle)
print_area(square)


# 4->>>>>  i =  Interface Segregation Principle

from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape, ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass



class Square(Rectangle):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def get_width(self):
        return self.side

    def get_height(self):
        return self.side



class CustomRectangle(Rectangle):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height



def print_area(shape):
    print(f"Area: {shape.area()}")



def print_rectangle_dimensions(rectangle):
    print(f"Width: {rectangle.get_width()}, Height: {rectangle.get_height()}")




square = Square(5)
custom_rectangle = CustomRectangle(4, 6)


print_area(square)


print_area(custom_rectangle)
print_rectangle_dimensions(custom_rectangle)

# 5 - >>>>> d = Dependency Inversion Principle


class SwitchableDevice:
    def operate(self):
        pass

class LightBulb(SwitchableDevice):
    def operate(self):
        return "LightBulb is ON"

class Fan(SwitchableDevice):
    def operate(self):
        return "Fan is ON"
class Switch:
    def __init__(self, device: SwitchableDevice):
        self.device = device

    def operate_device(self):
        return self.device.operate()

light_bulb = LightBulb()
fan = Fan()

switch_for_light = Switch(light_bulb)
print(switch_for_light.operate_device())
switch_for_fan = Switch(fan)
print(switch_for_fan.operate_device())
