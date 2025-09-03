f= open("demo1.txt","r")
data = f.readline()
print(data)
print(type(data))

data = f.readline()
print(data)

f.close()