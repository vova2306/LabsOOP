class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        return ((self.perimeter() / 2) * ((self.perimeter() / 2) - self.a) * ((self.perimeter() / 2)
                                                                              - self.b) * (
                        (self.perimeter() / 2) - self.c)) ** (1 / 2)


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Trapeze:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return ((self.a + self.b)/2) * ((self.c ** 2 - (((self.a - self.b) ** 2 + self.c**2 - self.d ** 2)
                               / (2 * abs(self.a - self.b)))) ** (1 / 2))


class Parallelogram:

    def __init__(self, a, b, height):
        self.a = a
        self.b = b
        self.height = height

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        if self.a == self.b:
            return self.a * self.height
        elif self.a > self.b and self.b > self.height:
            return self.a * self.height
        elif self.a > self.b and self.b < self.height:
            return self.b * self.height
        elif self.a < self.b and self.a > self.height:
            return self.b * self.height
        elif self.a < self.b and self.a < self.height:
            return self.a * self.height


from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

f = open(input(), 'r')
LeadPerimeter = 0
LeadArea = 0
line = f.readline().split()
while line:
    for i in range (1, len(line)):
        line[i] = float(line[i])
    dict_s = {'Triangle': Triangle, 'Circle': Circle, 'Rectangle': Rectangle, 'Trapeze': Trapeze, 'Parallelogram': Parallelogram}
    for i in range(1, len(line)):
        if line[i] == 0:
            continue
    if dict_s[line[0]] == Circle:
        perimeter = (dict_s[line[0]](line[1]).perimeter())
        area = (dict_s[line[0]](line[1]).area())
    elif dict_s[line[0]] == Parallelogram or dict_s[line[0]] == Parallelogram:
        perimeter = (dict_s[line[0]](line[1], line[2]).perimeter())
        area = (dict_s[line[0]](line[1], line[2]).area())
    elif dict_s[line[0]] == Triangle:
        perimeter = (dict_s[line[0]](line[1], line[2], line[3]).perimeter())
        area = (dict_s[line[0]](line[1], line[2], line[3]).area())
    elif dict_s[line[0]] == Trapeze:
        perimeter = (dict_s[line[0]](line[1], line[2], line[3], line[4]).perimeter())
        area = (dict_s[line[0]](line[1], line[2], line[3], line[4]).area())
    if LeadPerimeter < perimeter:
        LeadPerimeter = perimeter
        LP = line
    if LeadArea < area:
        LeadArea = area
        LA = line
    line = f.readline().split()

print(LP, 'perimeter:', LeadPerimeter)
print(LA, 'area:', LeadArea)
f.close()