class Instructors:
    companyName = "Bluelime"

    def __init__(self, course, duration):    # Python built-in function - Intializer
        self.course = course
        self.duration = duration

    def printInfo(self):
        print("My company name is", Instructors.companyName)


# Instantiating a class
elearning = Instructors("Python for beginners", 7)
bls = Instructors("Django for beginners", 8)

# Changing class attribute value
bls.course = "HTML"

# Accesing a clss method
elearning.printInfo()

# Accessing a class attribute
print(bls.course)
print(elearning.course)
print(bls.duration)

# Remove an atrribute
del bls.duration
