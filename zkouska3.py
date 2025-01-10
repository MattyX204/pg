# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

import math

class Shape():  #zakladni trida

    def area(self):
        return 0.0

class Rectangle(Shape):  #podtrida tridy Shape
    def __init__(self,width,height):  #nastavuje atributy tridy
        self.width = width
        self.height = height

    def area(self):  #metoda area ze zakladni tridy Shape
        return self.width * self.height   #vypocita obsah obdelniku
    
class Circle(Shape):  
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
        

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
