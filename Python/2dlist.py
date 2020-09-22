fruits = [
    ["apples", "berries", "kiwi"],
    ["oranges", "berries", "plums"],
    ["mangoes", "bananas", "coconuts"],
    ["pineapples"]
]

# Accessing element in 2D list
print(fruits[1][1])
print("\n")
for row in fruits:
    for col in row:
        print(col)
