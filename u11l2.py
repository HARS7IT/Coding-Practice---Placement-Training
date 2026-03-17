#deque:

from collections import deque
dq= deque([1, 2, 3])
dq.append(4)
dq.appendleft(8)
print(dq)

from collections import defaultdict

d= defaultdict(str)
d["a"]+="hv"
print(d)
print(d["a"])

d= defaultdict(int)
d["a"]+=1
d["b"]+=2
print(d)
print(d["c"])

from collections import namedtuple
Student= namedtuple("Student", ["name", "age", "marks"])
s1=Student("Hv", 21, 60)
print(s1.name)
print(s1.age)
print(s1.marks)





