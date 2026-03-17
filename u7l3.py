class Details_mark:
    def __init__(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def maxMarks(self):
        return max(self.sub1,self.sub2,self.sub3)
    def findavg(self):
        return (self.sub1+self.sub2+self.sub3)/3

s1=Details_mark(80,90,100) 
print(s1.maxMarks())
print(s1.findavg())

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
s1=Employee()
s1.display("HV",42,500000,"CSE-GT",21)
print("Salary after hike: ")
print(self.salary_after_hike)
    