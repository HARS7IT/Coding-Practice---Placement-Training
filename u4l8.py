person=("Alice",21,"Computer science")
print("Name:", person[0])
print("Age:", person[1])
print("Major:", person[2])

len_person=len(person)
print(len_person)

coordinates=("Bob",20,"Physics")
(x, y, z)=coordinates
print("Name:", x)
print("Age:", y)
print("Major:", z)

n=int(input("Enter the number of inputs:"))
temp_list=[]
for i in range(1, n+1):
    elements=int(input(f"Enter the element{i}:"))
    temp_list.append(elements)

new_tuple=tuple(temp_list)
print(new_tuple)


n=int(input("enter how many inner tuples: "))
outer_list=[]
for i in range (1,n+1):
    print(f"Inner tuples:")
    a=int(input("Enter number1:"))
    b=int(input("Enter number2:"))
    inner_tuple=(a,b)
    outer_list.append(inner_tuple)

new_tuple=tuple(outer_list)
print("New Tuple:", new_tuple)


