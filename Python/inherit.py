# Inheritance in Python
class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)


florist = Person("Jane", "Flowers")
florist.printName()
print("\n")


class Lawyers(Person):   # Inherit from Person class
    def __init__(self, fname, lname, caseType):
        Person.__init__(self, fname, lname)
        self.caseType = caseType
        #self.firstName = fname
        #self.lastName = lname

    def printInfo(self):
        print("Hello my name is", self.firstName, self.lastName)


happyLawyers = Lawyers("Jack", "Johnson", "criminal")
happyLawyers.printName()
happyLawyers.printInfo()

print(happyLawyers.caseType)
