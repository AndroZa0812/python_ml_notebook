import random as rn

class Shape:
    def __init__(self, name, location, color):
        self.name = name
        self.location = location
        self.color = color

    def draw(self):
        return f"id {id(self)}:\n name: {self.name}\n location: {self.location}\n color: {self.location}"

    def get_area(self):
        return 0


class Circle(Shape):
    def __init__(self, name, location, color, radius):
        super().__init__(name, location, color)
        self.radius = radius

    def draw(self):
        return super().draw() + f"\n radius: {self.radius}"


class Rectangle(Shape):
    def __init__(self, name, location, color, length, width):
        super().__init__(name, location, color)
        self.length = length
        self.width = width

    def draw(self):
        return super().draw() + f"\n width {self.width}\n length {self.length}"


def draw_shape(shape):
    print(shape.draw())


if __name__ == '__main__':
    shape_colors = ["red", "green", "orange", "yellow"]
    shapes = [Circle("circle",
                     (rn.randint(0, 10), rn.randint(0, 10)),
                     rn.choice(shape_colors),
                     rn.randint(0, 10)),
              Rectangle("rectangle",
              (rn.randint(0, 10), rn.randint(0, 10)),
              rn.choice(shape_colors),
              rn.randint(0, 10),
              rn.randint(0, 10))]

    for shape in shapes:
        draw_shape(shape)
