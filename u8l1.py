class Person:
    def __init__(self):
        self.name="Kannan"
        self.age=22
a=Person()
print("Name:",a.name)
print("Age:",a.age)


class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
a=Rectangle(10,5)
print("Length=",a.length)
print("Breadth=",a.breadth)


class Triangle:
    def __init__(self,breadth,height):
        self.breadth=breadth
        self.height=height

    def _display_(self):
        print("Area of triangle:",1/2*(self.breadth*self.height))
a=Triangle(3,4)
print("Breadth=",a.breadth)
print("Height=",a.height)
print("Area of triangle:")
a._display_()