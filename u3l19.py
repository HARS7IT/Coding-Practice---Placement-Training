n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

search=int(input("Enter element to count: "))
count=0
for item in my_list:
    if item == search:
        count+=1
print(search,"occurs",count,"times")