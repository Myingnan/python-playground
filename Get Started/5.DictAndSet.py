#--------------------------------
# 1. Dictionary
#--------------------------------

dict_1 = {
    "Michael": 95, 
    "Bob": 75, 
    "Tracy": 85
    }

# Get value from dict
temp = dict_1.get("Michael")
temp_2 = dict_1.get("cesc", -1)
print(temp)
print(temp_2)

# Whether an element in the dict
print("Bob" in dict_1)

# Insert value to dict
dict_1['Jack'] = 90
print(dict_1)

# Remove a key
print(dict_1.pop("Bob"))
print(dict_1)

#--------------------------------
# 2. Set
#--------------------------------
set_1 = set([1, 2, 3, 3])
print(set_1)

# Insert element to set
set_1.add(4)
print(set_1)

# Remove element in set
set_1.remove(4)
print(set_1)

# Combine
set_2 = set([2, 3, 4])
print(set_1 & set_2)
print(set_1 | set_2)



