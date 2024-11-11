from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    def __init__(self, color, center_x, center_y):
        self.color = color
        self.center_x = center_x
        self.center_y = center_y

    @abstractmethod
    def area(self):
        pass

    def display_color(self):
        return f"Колір фігури: {self.color}"

    def display_center(self):
        return f"Координати центру описаного кола: ({self.center_x}, {self.center_y})"

    def draw(self):
        print(f"Малювання фігури: {self.__class__.__name__}")
        print(self.display_color())
        print(self.display_center())
        print(f"Площа: {self.area()}\n")


class Circle(Shape):
    def __init__(self, color, center_x, center_y, radius):
        super().__init__(color, center_x, center_y)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, color, center_x, center_y, width, height):
        super().__init__(color, center_x, center_y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, color, center_x, center_y, side_a, side_b, side_c):
        super().__init__(color, center_x, center_y)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(self, color, center_x, center_y, *args):
        pass


class CircleFactory(ShapeFactory):
    def create_shape(self, color, center_x, center_y, radius):
        return Circle(color, center_x, center_y, radius)


class RectangleFactory(ShapeFactory):
    def create_shape(self, color, center_x, center_y, width, height):
        return Rectangle(color, center_x, center_y, width, height)


class TriangleFactory(ShapeFactory):
    def create_shape(self, color, center_x, center_y, side_a, side_b, side_c):
        return Triangle(color, center_x, center_y, side_a, side_b, side_c)


def user_interface():
    print("Виберіть фігуру для малювання:")
    print("1 - Коло")
    print("2 - Прямокутник")
    print("3 - Трикутник")
    choice = input("Ваш вибір: ")

    color = input("Введіть колір фігури: ")
    center_x = float(input("Введіть координату X центру фігури: "))
    center_y = float(input("Введіть координату Y центру фігури: "))

    shape = None

    if choice == '1':
        radius = float(input("Введіть радіус кола: "))
        factory = CircleFactory()
        shape = factory.create_shape(color, center_x, center_y, radius)
    elif choice == '2':
        width = float(input("Введіть ширину прямокутника: "))
        height = float(input("Введіть висоту прямокутника: "))
        factory = RectangleFactory()
        shape = factory.create_shape(color, center_x, center_y, width, height)
    elif choice == '3':
        side_a = float(input("Введіть сторону A трикутника: "))
        side_b = float(input("Введіть сторону B трикутника: "))
        side_c = float(input("Введіть сторону C трикутника: "))
        factory = TriangleFactory()
        shape = factory.create_shape(color, center_x, center_y, side_a, side_b, side_c)
    else:
        print("Невірний вибір фігури.")
        return

    shape.draw()

if __name__ == "__main__":
    user_interface()
