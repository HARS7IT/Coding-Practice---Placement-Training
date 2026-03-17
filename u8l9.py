class Calculator:
    def add(self,*args):
        return sum(args)
    
calc = Calculator()
print(calc.add(5,10))     
print(calc.add(5,10,15))
print(calc.add(1,2,3,4))

#run-time polymorphism using method overriding and compile-time ploymorphism using method overloading

class Animal:
    def speak(self):
        return "I am Animal."
class Dog(Animal):
    def speak(self):
        return "Woof"
print(Dog.speak())