import math

class Shape:
    def __init__(self, num_sides, side_lengths):
        if num_sides > 0:
            self.num_sides = num_sides
            self.side_lengths = side_lengths
        else:
            raise ValueError('The lengths are not of the correct value')

    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

class Triangle(Shape):
    def __init__(self, num_sides, side_lengths):
        Shape.__init__(self, num_sides, side_lengths)
    def area(self):
        a = self.side_lengths[0]
        b = self.side_lengths[1]
        c = self.side_lengths[2]
        s = (a + b + c) / 2
        return math.sqrt(s * ((s - a) * (s - b) * (s - c)))

class Rectangle(Shape):
    def __init__(self, num_sides, side_lengths):
        Shape.__init__(self, num_sides, side_lengths)


class Square(Rectangle):
    def __init__(self, num_sides, side_lengths):
        Rectangle.__init__(self, num_sides, side_lengths)

rect = Rectangle(4, [2, 4])
print(rect.area())
tr1 = Triangle(3, [3, 4, 5])
print(tr1.area())
