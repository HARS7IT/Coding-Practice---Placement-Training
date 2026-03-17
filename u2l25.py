for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i)
    print("*")


from sre_constants import JUMP
for num in [20,11,9,66,4,89]:
    if num%2!=0:
        continue 
    print(num)


for letter in "python":
    if letter=="h":
        continue
    print("Current number: ", letter)