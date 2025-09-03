# print number from 1 to 100 
i = 1
while i <= 100:
    print(i)
    i += 1
 
# print number from 100 to 1

i = 100
while i >= 1 : # this is stoping codition 
    print(i)
    i -= 1

# print the multiplication table of a number n .
n = int(input("enter a number :"))
i = 1 
while i<= 10:
    print( n * i)
    i += 1

# print the element of the following list using a loop :
# [ 1,4,9,16,25,36,49,64,81,100]

num = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(num): 
    print(num[idx])
    idx += 1
