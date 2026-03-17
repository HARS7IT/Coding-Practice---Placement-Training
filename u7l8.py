#Multiple Inheritance

class Parent1:
    def p1():
        print("I am parent 1")
        
class Parent2:
    def p2():
        print("I am parent 2")

class Child(Parent1,Parent2):
    def c():
        print("I am child")

plobj=Child
plobj.c()
plobj.p1()
plobj.p2()


