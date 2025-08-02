inventory = ["sword", "armor", "shield", "boots"] # list. works similar to C# List but can be a list of different types
print(inventory)
print(type(inventory))

inventory.append("spear") # append add to the end of the list
print(inventory)

inventory.insert(0, "guitar") # instert at index. takes an index and an value to insert
print(inventory)

inventory.pop() # removes last item in list
print(inventory)

universe = [[1, 2, 3], # list of lists or matrix.
            [4, 5, 6], # laid out this was to clearly see rows and cols
            [7, 8, 9],
            [1, 2, 3],
            [4, 5],
            [6]] # row index 5 col index 0

last_element = universe[5][0]
print(last_element) # prints value at above index

item = ('Health Kit', 4) # this is s a tuple in py. they are immutable and cannot be modified
print(item)
print(type(item))

name = item[0] # assigning name var with val from item tuple
number_of_kits = item[1]
print(type(name)) # py knows name is type str. tuple hols different types

print(item.count('Health Kit')) # this prints out the number of times 'Health Kit' is listed in the tuple
print(item.index('Health Kit')) # this prints out the index of 'Health Kit' in the tuple

dictionary_inventory = {'Knife' : 1, 'Bow' : 1, 'Potion' : 2, 'Arrow' : 1} # this is a dicitonary. kvp are mutable
print(dictionary_inventory)
print(type(dictionary_inventory))

dictionary_inventory['Arrow'] = 5
dictionary_inventory['Wings'] = 2 # this appends a new kvp since the key 'Wings' isn't in the dict
print(dictionary_inventory)

print(dictionary_inventory.get("Silver")) # 'Silver' is not in the dict but the 'get' function will return 'none' instead of crashing
print(dictionary_inventory.keys())
print(dictionary_inventory.values())
print(dictionary_inventory.items()) # this is a list of tuples or key value pairs

dictionary_inventory.pop('Arrow') # removes the kvp at key 'Arrow'

first_ten = range(10) # range of numbers 0-9
print(first_ten)
print(type(first_ten))

first_ten_natural = range(1, 11) # this creates a range of number 1 - 10.
print(first_ten_natural[0])
print(first_ten_natural[9]) # this is index 9 so value will be 10
print(type(first_ten_natural))

reversed_first_ten_natural = reversed(first_ten_natural) # reversing the range
reversed_first_ten_natural = list(reversed_first_ten_natural) # casting the range to a list
print(reversed_first_ten_natural) #print the reversed list
print(type(reversed_first_ten_natural)) # data type is now list