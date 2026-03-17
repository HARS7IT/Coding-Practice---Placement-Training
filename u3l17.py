n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

min_val=my_list[0]
for num in my_list:
    if num<min_val:
        min_val=num
print("Minimum element is: ",min_val)