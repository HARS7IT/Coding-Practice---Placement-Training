n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

reversed_list=[]
for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])
print("Reversed list: ",reversed_list)