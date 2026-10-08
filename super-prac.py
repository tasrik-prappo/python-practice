class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"Radius: {self.radius} and Area: {3.1416 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, is_filled, length):
        super().__init__(color, is_filled)
        self.length = length

    def describe(self):
        super().describe()
        print(f"Length: {self.length} and Area: {self.length * self.length}")

class Triangle(Shape):
    def __init__(self, color, is_filled, height, length):
        super().__init__(color, is_filled)
        self.height = height
        self.length = length

    def describe(self):
        super().describe()
        print(f"Height: {self.height}, Length: {self.length}, and Area: {0.5 * self.height * self.length}")


# Execution
triangle = Triangle("Red", True, 10, 20)
triangle.describe()
print("---")
square = Square("Blue", False, 10)
square.describe()
print("---")
circle = Circle("Green", True, 5)
circle.describe()