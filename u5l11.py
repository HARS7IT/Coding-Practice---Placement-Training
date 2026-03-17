def separate_num(list):
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        elements=int(input(f"Enter the element {i}: "))
        list.append(elements)
        print(list)
        sum_positive=0
        sum_negative=0
        
        for num in list:
            if num>0:
                sum_positive+=num
            elif num<0:
                sum_negative+=num
            else:
                print("Invalid Number")
        
    print("Positive sum: ",sum_positive)
    print("Negative sum: ",sum_negative)
list=[]
separate_num(list)