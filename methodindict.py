# method in dict 

# myDict.keys() (return all keys )

info = {
    "key" : "values",
    "name" : "apnacollege",
    "learning" : "coding",
    "age" : 35,
    "is adult" : True,
}
print(info.keys())

#my dict.values () (return all values )

print(info.values())

# my dict.items() (returns all (key,val) pairs as tuple )

print(info.items())

# my dict.get("key" (return the key according to value ))

print(info["name"]) # error 
print(info.get("name")) # it don't gives error return the values none 


# myDict.update(newDict ) (insert the specified items to the dictionary)

info.update({"city": "delhi "})
print(info)
