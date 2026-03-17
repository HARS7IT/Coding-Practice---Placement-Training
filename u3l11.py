user_input=input("Enter the numbers separated by space: ")
numbers=list(map(int,user_input.split()))
minimum=min(numbers)
maximum=max(numbers)\

print("Maximum value: ",maximum)
print("Minimum value: ",minimum)