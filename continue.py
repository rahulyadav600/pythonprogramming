# continue terminate execution in the current iteration and continue execution of the loop
# with the next 
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i +=1