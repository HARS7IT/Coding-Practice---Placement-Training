#static
class Employee:

    company="Google"   #static data
    def __init__(self,name,eid,role,salary):
        self.name=name
        self.eid=eid
        self.role=role
        self.salary=salary

    def display(self):
        return (f'{self.name},{self.eid},{self.role},{self.salary},{Employee.company}')
    
    def __str__(self):
        return (f'{self.name},{self.eid},{self.role},{self.salary},{Employee.company}')

obj1=Employee("hv",101,"software dev",2000000)
print(obj1)

