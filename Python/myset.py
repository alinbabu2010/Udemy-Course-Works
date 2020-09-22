fruits = {"grapes", "apples", "oranges"}

# Looping through set elements
for x in fruits:
    print(x)
print("\n")

# Construct set using constructor function
animals = set(("lion", "tiger", "bear"))
for y in animals:
    print(y)
print("\n")

print(len(animals))
print("\n")

# add() - Adds an element to set
fruits.add("berries")
print(fruits, "\n")

# update() - Add mulitple items to set
fruits.update(["bananas", "mango"])
print(fruits, "\n")

# discard() - Removes a specified element or item
fruits.discard("berries")
print(fruits, '\n')

# remove() - Removes a specified element or item
fruits.remove("mango")
print(fruits, '\n')

# clear() - Remove all elements in a set
fruits.clear()
print(fruits)

# del() - Delete the set
del animals
