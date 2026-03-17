n=int(input("Enter number of elements: "))
my_list=[]
for i in range(n):
    my_list.append(int(input("Enter number: ")))

even_list=[]
odd_list=[]
for num in my_list:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)




print("Even Numbers: ",even_list)
print("Odd numbers: ",odd_list)