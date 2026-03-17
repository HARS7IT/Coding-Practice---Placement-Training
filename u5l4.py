def my_function(list):
          n=int(input("Enter the number of elements: "))
          for i in range(n):
             i=int(input("Enter number {i}: "))
             list.append(i)
             print(list)
my_fruits=[]
my_function(my_fruits)