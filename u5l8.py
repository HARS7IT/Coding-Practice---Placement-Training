def sum_list(list):
    n=int(input("Enter the number of items in a list: "))
    for i in range(n):
        elements=int(input(f"Enter the elements {i}: "))
        list.append(elements)
        print(list)
        total=0
        for num in list:
          total+=num
    print("Total sum: ",total)
list=[]
sum_list(list)

#* is used to pass 1 argumment
#** is used to pass 2 arguments
