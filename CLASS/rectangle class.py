class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area_of_rectangle(self):
        # return self.length * self.width
        print(f"Area of Rectangle is :- {self.length * self.width}")

    def perimeter_of_Rectangle(self):
        # return 2 * (self.length + self.width)
        print(f"Perimeter of Rectangle is :- {2 * (self.length + self.width)}")

get_rectangle1 = Rectangle(length=5,width=6)
get_rectangle1.area_of_rectangle()
get_rectangle1.perimeter_of_Rectangle()
get_rectangle1.length