# Defining and calling of a function
def sum(x, y):
    print(x + y)


a = 75
b = 25
sum(a, b)


# Return value in a function
def sub(x, y):
    return x - y


print(sub(56, 36))


# Using default parameter value
def students_name(names="Billu"):
    print("Hello " + names)


students_name()
students_name("John")
students_name("Jack")


# Using keyword arguments
def more_num(a, b=7, c=10):
    print("a is ", a, "and b is ", b, "while c is ", c)


more_num(3, 17)
more_num(23, c=17)
more_num(c=40, a=80)


# Function returning other function
def greeting():
    def say_hello():
        return "Hello"
    return say_hello


hello = greeting()
print(hello())


# Assigning functions to varaibles
def mynum(x):
    return x + 1


num = mynum
print(num(9))
print(mynum(19), "\n")


# Global and local variable scope
x = 10


def my_numbers():
    global x
    print(x)
    x = 7
    print("My favorite number is ", x)


my_numbers()
print(x)


# Nesting Functions
def mynum(a):
    def num(a):
        return a + 1
    result = num(a)
    return result


print(mynum(4))


# Nesting Function accesing variable scope
def display_message(message):
    "Hello"

    def message_sender():
        "Nested function"
        print(message)
    message_sender()


display_message("Show me the money.")


# Function pass keyword
def dream_home():
    pass


# Pass function as arguments
def mynum(b):
    return b + 1


def addnum(c):
    newnum = 7
    return c(newnum)


print(addnum(mynum))


# Variable argumnet parameter
def total_number(a=7, *numbers, **phonebook):
    print("My favorite number is ", a)
    for num in numbers:
        print("num", num)
    for name, phone_number in phonebook.items():
        print(name, phone_number)


total_number(7, 1, 2, 3, Jane=222, John=444, Angela=5555)


# Python methods
b = "hello"
print(len(b))
b.upper()
print(b)


# Python anonymous function - lambada
def a(b): return b + 4


print(a(4))


def c(d, e): return d + e


print(c(7, 8))


def ghost_number(n):
    return lambda f: f * n


double_num = ghost_number(2)
print(double_num(20))


# Python DocStrings
def add_numbers(d, e):
    ''' Adding two numbers.

            The values must be integers '''
    print(d + e)


add_numbers(8, 4)
print(add_numbers.__doc__)
