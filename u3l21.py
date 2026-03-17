n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i]>my_list[j]:
            my_list[i], my_list[j] = my_list[j],my_list[i]

print("Sorted list: ",my_list)