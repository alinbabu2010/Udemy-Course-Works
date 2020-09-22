fruits = ("grapes", "apples", "orange")

# Looping through elements in tuple
for x in fruits:
    print(x)
print("\n")

# Accesing elements in tuple
print(fruits[2])
print("\n")

# Constructing tuple using tuple constructor
animals = tuple(("lion", "tiger", "fox"))
print(animals)
print("\n")
print(len(animals))
print("\n")

# animals.add("dog")  # Error will occur no addition can be added.
# animals[0] = "cheetah"  # Error will occur no addition can be added.
del animals
print(animals)
