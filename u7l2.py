class Student:
    def __init__(self,name,roll,branch,age):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.age=age
    def display(self):
        print(f"{self.name},{self.roll},{self.branch},{self.age}")
s1=Student("HV",42,"CSE-GT",21)
s1.display()

class Details_mark:
    def __init__(self,marks,sub1,sub2,sub3):
        self.marks=marks
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def maxMarks(self):
        return max(self.sub1,self.sub2,self.sub3)
    def findavg(self):
        return (self.sub1+self.sub2+self.sub3)/3

s1=Details_mark() 
print(s1.maxMarks())