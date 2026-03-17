user_input=input("Enter a string: ")

reversed_string=user_input[::-1]#scope resolution operator
print("Reversed string: ",reversed_string)

#program to remove duplicate characters

user_input=input("Enter the string: ")
seen=set()
result=""

for char in user_input:
    if char not in seen:
        seen.add(char)
        result+=char


