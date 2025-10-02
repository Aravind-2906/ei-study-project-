# Factory Pattern demo: Shape Factory
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class ShapeFactory:
    @staticmethod
    def create(shape_type):
        if shape_type == "circle": return Circle()
        if shape_type == "square": return Square()
        raise ValueError("Unknown shape")


s1 = ShapeFactory.create("circle")
s2 = ShapeFactory.create("square")
s1.draw(); s2.draw()
