#open close princible
# class shape :
#     def area (self):
#         pass
#
# class ractangle (shape) :
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height    
#
#     def area (self) :
#         return self.width* self.height
#
# class circle (shape):
#     def __init__ (self,radius):
#         self.radius=radius
#
#     def area (self):
#         return 3.14 * self.radius * self.radius
#
# class tringle :
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#
#     def area (self):
#         return 0.5 * self.base *self.height
#
#
# a=circle(5)
# print(a.area())
#
# b=tringle(5,6)
# print(b.area())



#likovs substitution principle

#
# class ractangle :
#     def __init__(self,width,hieght):
#         self.width=width
#         self.hieght=hieght
#
#     def setwidth (self,width):
#         self.width=width
#     def sethieght (self,hieght):
#         self.hieght=hieght
#
#     def get_area (self):
#         return self.width * self.hieght


# class squere(ractangle) :
#     def __init__(self,width,hieght):
#         ractangle .__init__(self,width,hieght)
#
#     def setwidth (self,width):
#         self.width=width
#         self.hieght=width
#     def sethieght (self,hieght):
#         self.hieght=hieght
#         self.width=hieght
#
#
# def print_area(Rectangle) :
#     Rectangle.setwidth(5)
#     Rectangle.sethieght(10)
#     area=Rectangle.get_area()
#     print(f"The area is {area}")
#
#
# Rectangle = ractangle(5,4)
#
# Squere=squere(5,5)
#
# print_area(Rectangle)
# print_area(Squere)

#*******************************************************************************
# class Bird:
#     def fly(self):
#         return "I can fly"
#
# class Penguin(Bird):
#     # Penguins cannot fly, so we override the fly method
#     def fly(self):
#         return "Sorry, I can't fly"
# def make_bird_fly(bird):
#     return bird.fly()
#
# # Using Bird
# bird = Bird()
# print(make_bird_fly(bird))  # Output: "I can fly" (as expected)
#
# # Using Penguin (violating LSP)
# penguin = Penguin()
# print(make_bird_fly(penguin))  # Output: "Sorry, I can't fly" (as expected)
#
# # However, using LSP, we should be able to substitute a base class with its derived class without affecting behavior
# bird_as_penguin = Penguin()
# print(make_bird_fly(bird_as_penguin))  # Output: "Sorry, I can't fly" (as expected)
#
# # Now, let's assume the LSP is not violated
# bird_as_penguin_but_not_really = Bird()
# print(make_bird_fly(bird_as_penguin_but_not_really))  # Output: "I can fly" (unexpected behavior)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def set_width(self, width):
#         self.width = width
#
#     def set_height(self, height):
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Square(Rectangle):
#     def __init__(self, side_length):
#         # A square has equal sides, so we initialize it with one side length
#         super().__init__(side_length, side_length)
#
#     # Overriding set_width and set_height to maintain square properties
#     def set_width(self, width):
#         self.width = self.height = width
#
#     def set_height(self, height):
#         self.width = self.height = height
# def calculate_area(rectangle,width,height):
#     # Assume the rectangle's width and height can be set independently
#     rectangle.set_width(width)
#     rectangle.set_height(height)
#     return rectangle.area()
#
# # Using Rectangle
# rectangle = Rectangle(10,10)
# print(calculate_area(rectangle,10 ,10))  # Output: 20 (as expected)
#
# # Using Square (violating LSP)
# square = Square(5)
# print(calculate_area(square , 7 ,6))  # Output: 25 (unexpected behavior)

from abc import ABC, abstractmethod

class AreaClac (ABC):
    @abstractmethod
    def calc_Area (self):
        pass
class perimterecala (ABC):
    @abstractmethod
    def perimterecala (self):
        pass
class Circle (AreaClac,perimterecala) :
    def __init__(self,redius):
        self.redius=redius
    def calc_Area(self):
        return  3.14 * self.redius *self.redius

    def perimterecala(self):
        return  2 * 3.14 * self.redius

class Ractangle (AreaClac,perimterecala) :
    def __init__(self,width,height):
        self.redius=width
        self.height=height
    def calc_Area(self):
        return  self.width * self.height

    def perimterecala(self):
        return  2 * (self.width + self.height )

circle=Circle(3)
print(circle.calc_Area())
print(circle.perimterecala())