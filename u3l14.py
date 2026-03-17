for i in range(1,6):
    for j in range(0,i):
        print(i,end="\t")
    print("")


vowels=["a","e","i","o","u","A","E","I","O","U"]
results=""

string=input("Enter the string: ")
for i in range(len(string)):
    if string[i] not in vowels:
        results=results+string[i]

print("\nAfter removing the vowels: ",results)

    
