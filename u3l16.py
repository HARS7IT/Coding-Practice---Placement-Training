n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

max_val=my_list[0]
for num in my_list:
    if num>max_val:
        max_val=num
print("Maximum element is: ",max_val)