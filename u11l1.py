setA={1, 2, 3, 4}
setB={2, 3, 4, 5}
print("Union", setA | setB)
print("Intersection", setA & setB)


from collections import Counter
items= ["apple", "grape", "banana", "mango"]

count = Counter(items)
print("before update:", count)

count.update(["apple", "flask"])
print("after update", count)
for key, value in count.items():
    print(key, value)