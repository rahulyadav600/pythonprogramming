#append method 
marks = [34,44,32,21,21,56]
print(marks)
marks.append(99)
print(marks)

# sorting method in list (asscending order)
list = [7,8,9,3,4,5,6]
print(list.sort())
print(list)

# sorting method in list (descending order )
list2 = [3,4,5,6,7,8,9,10]
print(list2.sort(reverse=True))
print(list2)

#reverse method reverse the complete original string 

list3 = [ "rahul", "tannu","winny"]
list3.reverse()
print(list3)


#insert method (insert element at index )
list4 = [3,4,5,2,5]
list4.insert(1, 9)
print(list4)

# remove method (remove first occcurence of elemnet )

list5 = [2,3,4,5]
list5.remove(5)
print(list5)

# pop method (remove the element at index)

list6 = [2,5,6,4,3]
list6.pop(2)
print(list6)