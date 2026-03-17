x = lambda a : a+10#lambda function
print(x(5))


#if we take two arguments
x=lambda a, b: a*b
print(x(2,3))


def separate_num(list):
    n=int(input("Enter the number of elements: "))
    for i in range(n):
        elements=int(input(f"Enter the element {i}: "))
        list.append(elements)
        print(list)
        even_count=0
        odd_count=0
        even_total=0
        odd_total=0
        for num in list:
            if num%2==0:
                even_count+=1
                even_total+=num
            else:
                odd_count+=1
                odd_total+=num
    print("Even count: ",even_count)
    print("Odd count: ",odd_count)
    print(even_total)
    print(odd_total)
list=[]
separate_num(list)