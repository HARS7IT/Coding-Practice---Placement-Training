n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

unique_list=[]
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates: ",unique_list)