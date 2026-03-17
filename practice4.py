n=int(input("REnter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()