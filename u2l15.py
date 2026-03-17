word=input("Enter word: ")
for char in word:
    if char == "a":
        print("Found 'a'  stop looping !!!")
        break
    print(char)


word=input("Enter word: ")
for char in word:
    if char == "a":
        print("Found 'a' !!!")
        continue
    print(char)