#replace all occurences of first char with $

user_input=input("Enter the string: ")
first_char=user_input[0]
result=first_char

for i in range(1,len(user_input)):
    if user_input[i] == first_char:
        result+="$"
    else:
        result+=user_input[i]

print("Modified String: ",result)