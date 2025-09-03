nums = [12,34,557,87,2322,487,8980,343,23,1221]
x = 87 
idx = 0 
for el in nums:
    if(el == x ):
        print("number found at the idx ", idx)
    else:
        print("finding....")
        idx += 1