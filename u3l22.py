n1=int(input("Enter number of elements in first list: "))
my_list1=[]
for i in range(n1):
    my_list1.append(int(input("Enter number: ")))

n2=int(input("Enter number of elements in second list: "))
my_list2=[]
for i in range(n2):
    my_list2.append(int(input("Enter number: ")))

merged_list=my_list1 + my_list2
print("Merged List: ",merged_list)