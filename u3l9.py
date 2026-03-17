#range function()
newlist=[x for x in range(10)]
print(newlist)

newlist=[x for x in range(10) if x<5]
print(newlist)

fruits=["apple","banana","cherry"]
newlist=[x.upper() for x in fruits]
print(newlist)

newlist=["hello" for x in fruits]
print(newlist)
