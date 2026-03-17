fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]

for x in fruits:
    if"a" in x:
        newlist.append(x)

print(newlist)

electronics=["mobile","headset","laptop","tablet"]
newlist=[]

for x in electronics:
    if "t"in x:
        newlist.append(x)

print(newlist)

#or another method

fruits=["apple","banana","cherry"]
newlist=[x for x in fruits if "a" in x]

print(newlist)

newlist=[x for x in fruits if x!="apple"]
print(newlist)