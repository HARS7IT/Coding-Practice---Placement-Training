class Employee:
    def __init__(self,name,eid,salary,branch,age):
        self.name=name
        self.eid=eid
        self.salary=salary
        self.branch=branch
        self.age=age
    def display(self):
        print(f"{self.name},{self.eid},{self.salary},{self.branch},{self.age}")
    def salary_after_hike(self):
        return (self.salary+(0.45*self.salary))
s1=Employee("HV",42,500000,"CSE-GT",21)
s1.display()
print("Salary after hike: ")
print(s1.salary_after_hike())


import datetime
dir(datetime)


