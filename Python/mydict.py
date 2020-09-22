mycar = {
    "brand": "Range Rover",
    "model": "HSE",
    "year":  2017
}

print(mycar)

# Create dictionary using constructor method
mygreens = dict(fruit="green apples", vegetables="kale")
print(mygreens, "\n")

# number of key value pairs
print(len(mycar))

# Change the value of a key
mycar["year"] = 2020
print(mycar, "\n")

# get() - Returns the value of a specified key
print(mycar.get("year"), "\n")

# update() - Inserts a specified key:value pair in dictionary
mycar.update({"color": "silver"})
print(mycar, "\n")

# keys() - Returns a list of dictionary keys.
b = mycar.keys()
print(b, "\n")

# values() - Returns a list of dictionary values.
b = mycar.values()
print(b, "\n")

# pop() - Remove the key:value pairs
mycar.pop("color")
print(mycar, "\n")

# clear() - Removes all key:ve pairs in dictionary
mycar.clear()
print(mycar)

# del() - Deletes the dictionary
del mycar
