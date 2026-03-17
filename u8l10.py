#operator overloading

#"__add__ method " within the vector class is a special method that defines how the + operator operator behaves for Vector objects. This allows the user to add two vectors using the familiar +symbol, which is a form of syntactic sugar

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x},{self.y})"
    
v1=Vector(2,4)
v2=Vector(3,6)
v3=v1+v2

print(v3)