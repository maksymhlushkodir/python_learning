import math


class Shape:
   def __init__(self):
       pass

   def area(self):
       raise NotImplementedError

   def perimeter(self):
       raise NotImplementedError

   def details(self):
       raise NotImplementedError


class Rectangle(Shape):
   def __init__(self, width: float, height: float):
       super().__init__()
       self.width = width
       self.height = height

   def area(self):
       print('---<Area>------------------------------------------------------------')
       area_rectangle = (self.width * self.height)
       print(f'Formula: width x height -> {self.width} x {self.height} -> {area_rectangle}')
       return area_rectangle

   def perimeter(self):
       print('---<Perimeter>--------------------------------------------------------')
       perimeter_rectangle = ((self.width * 2) + (self.height * 2))
       print(f'Formula: (width x 2) + (height x 2) -> ({self.width} x 2) + ({self.height} x 2) -> {perimeter_rectangle}')
       return perimeter_rectangle

   def details(self):
       return 'Rectangle'


class Circle(Shape):
   def __init__(self, radius: float):
       super().__init__()
       self.radius = radius

   def area(self):
       print('---<Area>------------------------------------------------------------')
       area_circle = (math.pi * (self.radius ** 2))
       print(f'Formula: pi * radius^2 -> pi x {self.radius}^2 -> {area_circle}')
       return area_circle

   def perimeter(self):
       print('---<Perimeter>--------------------------------------------------------')
       perimeter_circle = (math.pi * 2 * self.radius)
       print(f'Formula: pi x 2 x radius -> pi x 2 x {self.radius} -> {perimeter_circle}')
       return perimeter_circle

   def details(self):
       return 'Circle'


rectangle = Rectangle(5.5, 7)
circle = Circle(7.2)

# Calculate and print
print(rectangle.details())
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

print("-" * 20)

print(circle.details())
print(f"Area: {circle.area():.2f}")  # Limit to two decimal places for nice output
print(f"Perimeter: {circle.perimeter():.2f}") # Limit to two decimal places for nice output

