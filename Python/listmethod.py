fruits = ["berries", "apples", "grapes", "orange"]
vegetables = ["kale", "broccoli", "lettuce"]

# extend() - Combine one list to another list end
fruits.extend(vegetables)
print(fruits)

# append() - Append a new item at end of the list
vegetables.append("beans")
print(vegetables)

# sort() - Sort the item of list
vegetables.sort()
print(vegetables)
vegetables.sort(reverse=True)
print(vegetables)

# count() - Count the occurence of a element
print(fruits.count("berries"))

# index() - Find the index of a element
print(fruits.index("grapes"))

# insert() - Insert an item at specified index
fruits.insert(0, "banana")
print(fruits)

# pop() - Remove the last item
fruits.pop()
print(fruits)

# remove() - Remove a specific item
vegetables.remove("kale")
print(vegetables)

# del() - Delete a list or delete a specific item at an index
del fruits[0]
print(fruits)
del vegetables
print(vegetables)
