#polymorphism

class Animal:
    def make_sound(self):
        print("The animal makes a sound...")
class Dog(Animal):
    def make_sound(self):
        print("The dog barks...")
class Cat(Animal):
    def make_sound(self):
        print("The cat meows...")
def animal_sounds(animal):
    animal.make_sound()
a=Animal()
b=Dog()
c=Cat()
animal_sounds(a)
animal_sounds(b)
animal_sounds(c)