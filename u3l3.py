name="Artificial Intelligence"
print(name.count("intelligence"))


name="science"
print(name.find("e"))

#Whitespace methods

text="  HELLO  "
print(text.strip())#removes all spaces
print(text.lstrip())#removes left spaces
print(text.rstrip())#removes right spaces


#splitting and joining
text="apple,banana,orange"
fruits=text.split(",")
print(" * ".join(fruits))