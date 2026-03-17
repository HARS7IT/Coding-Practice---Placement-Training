names=["Ravi", "Sita", "Hv", "Aak"]
marks_data = [("Ravi",80),("Sita",90),("Ravi",85)]

from collections import Counter
count=Counter(names)
print(count)

from collections import deque
dq=deque(["Ravi", "Sita", "Hv", "Aak"])
dq.popleft()
print(dq)

from collections import defaultdict
d=defaultdict(int)
d["Ravi"]+=80
d["Ravi"]+=85
d["Sita"]+=90
print(d)
print(d["Ravi"])

from collections import namedtuple
Student=namedtuple("Student", ["name", "marks"])
s1=Student("Ravi", 80)
print(s1.name)
print(s1.marks)

