import math


class Calculator:

    def __init__(self, x):
        self.x = x

    def square(self):
        return self.x ** 2

    def qubic(self):
        return self.x ** 3

    def square_root(self):
        return self.x ** .5

    def logarithm(self):
        return math.log10(self.x)


class Scientific_Calculator(Calculator):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def sum(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


class Trignometry_math(Calculator):

    def __init__(self, x, y, angle):
        super().__init__(x)
        self.y = y
        self.angle = angle

    def sine(self):
        return math.sin(self.angle)

    def cosine(self):
        return math.cos(self.angle)

    def Tangent(self):
        return math.tan(self.angle)

    def cot(self):
        return 1 / (math.tan(self.angle))

    def cosec(self):
        return 1 / (math.sin(self.angle))

    def sec(self):
        return 1 / (math.cos(self.angle))


calculator = Trignometry_math(x=25, y=16, angle=math.pi / 4)
# m = Scientific_Calculator(x=25, y=16)
# n = Calculator(10)
print(calculator.square())
print(calculator.square_root())
print(calculator.qubic())
# print(calculator.sum())
print(calculator.logarithm())
print(calculator.cosine())
print(calculator.sine())
