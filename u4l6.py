numbers=[1,2,3,4,4,5]
unique_numbers = set(numbers)
print("Original list: ",numbers)
print("Unique numbers: ",unique_numbers)


frozen=frozenset(["a","b","c"])
print("Frozen set: ", frozen)
frozen.add("d")#not possible
print(frozen)