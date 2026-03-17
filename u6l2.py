import os
filename=input("Enter the name: ")
if os.path.isfile(f"C:\\Users\\Harshit\\Desktop\\PYTHON\\demofile.txt"):
    print("yes present")
    f=open("C:\\Users\\Harshit\\Desktop\\PYTHON\\demofile.txt")
    output=f.read()
    print(output)
else:
    print("No,not present")


f=open(r"C:\Users\Harshit\Desktop\PYTHON\demofile.txt","w")
f.write("annu\n")
list=["Ajay\n","Tamil\n","Nadu\n"]
f.writelines(list)
f.close()
print("File is closed or not:",f.closed)

f=open(r"C:\Users\Harshit\Desktop\PYTHON\demofile.txt")
output=f.readlines()
info="".join(output)
print(info)
print(output)
f.close()
print("File is closed or not:",f.closed)

f=open(r"C:\Users\Harshit\Desktop\PYTHON\demofile.txt","r")
print(f.tell())
output=f.read()
info="".join(output)
print(info)
print(f.tell())
f.close()
print("File is closed or not:",f.closed)

f=open(r"C:\Users\Harshit\Desktop\PYTHON\demofile.txt","r")
print(f.tell())
output=f.read()
info="".join(output)
print(info)
print(f.tell())
print(f.seek(20))
print(f.tell())
output=f.read()
print(output)
print(f.tell())
print(f.tell())
f.close()
print("File is closed or not:",f.closed)