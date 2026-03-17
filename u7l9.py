class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return f'{self.name},{self.age},{self.gender}'
    
class Student(Person):
    def __init__(self,name,age,gender,roll,branch):
        super().__init__(name,age,gender)
        self.roll=roll
        self.branch=branch

    def __str__(self):
        per_data=super().__str__()
        return(f'{per_data},{self.roll},{self.branch}')
    
class Employee(Person):
    def __init__(self,name,age,gender,eid,salary):
        super().__init__(name,age,gender)
        self.eid=eid
        self.salary=salary

    def __str__(self):
        per_data1=super().__str__()
        return(f'{per_data1},{self.eid},{self.salary}')
    
p1=Person("hv",21,"male")
s1=Student("hv",21,"Male",42,"CSE-GT")
e1=Employee("hv",21,"M",101,500000)
print(p1)
print(s1)
print(e1)