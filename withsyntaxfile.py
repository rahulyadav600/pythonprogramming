# with for read operation
with open("demo1.txt","r") as f:
    data = f.read()
print(data)

# with for write operation 

with open("demo1.txt","w") as f:
    f.write(" python is worldwide is very demanding language")
