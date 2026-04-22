class shape:
    def area(self):
        print("it is a shape")

class Circle(shape):
    def __init__(self,radius):
       self.radius=radius
       print("area",3.14*radius*radius )

c=Circle(int(input("enter a number: ")))       
       
