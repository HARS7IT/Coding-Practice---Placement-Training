n=int(input("Enter how many numbers?"))

even_num=0
odd_num=0

for i in range(n):
    a=int(input(f"Enter number {i+1}: "))
    if a%2 == 0:
        even_num+=a
    else:
        odd_num+=a

print("Sum of even numbers: ", even_num)
print("Sum of odd numbers: ", odd_num)