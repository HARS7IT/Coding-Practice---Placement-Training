f=open(r"C:\Users\Harshit\Desktop\PYTHON\demofile.txt")
print(f.read())

f=open("demofile.txt","w")
f.write("Hello again! This file is for testing purpose!!")
f.close()

f=open("demofile.txt")
print(f.read())

f=open("demofile.txt","a")
print("file name is",f.name)
print("file mode is:",f.mode)
print("file property is",f.readable())
print("file property is",f.writable())
print("file is closed (or) not",f.closed)
f.close()
print("file is closed (or) not",f.closed)