#Inheritance:

#single inheritance:
class Animal:
    def eating():
        print("Eating..")
    def sound():
        print("Sound..")

class Lion(Animal):
    def eat():
        print("Lion eats flesh")
    def sound():
        print("Lion roars")

lobj=Lion
lobj.eat()
lobj.eating()