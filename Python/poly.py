# Polymorphism in Python #

# polymorphism in bulit-in function
print(len("Hello"))
print(len([20, 40, 80]))

# polymorphism in unction


def addNumbers(a, b, c=1):
    return a + b + c


print(addNumbers(8, 9))
print(addNumbers(8, 9, 4))

# Polymorphism using class


class UK():
    def capitalCity(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language")


class Spain():
    def capitalCity(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language")


queen = UK()
queen.capitalCity()

zara = Spain()
zara.capitalCity()
print("\n")

for country in (queen, zara):
    country.capitalCity()
    country.language()
    print("\n")

# Creatimg polymorphism by using exisitng methods on a new function


def Europe(eu):
    eu.capitalCity()


print("\n")
Europe(queen)
Europe(zara)
