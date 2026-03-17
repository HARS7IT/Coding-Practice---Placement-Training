def name(a,b):#parameter
    name(5,7)#argument


user_input=input("Enter the string: ")
freq={}#dictionary creation

for char in user_input:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

print("Character frequencies: ")
for char in freq:
    print(char,":",freq[char])

