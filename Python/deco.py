# Python Decorators
def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper


@my_decorator
def say_hello():
    return "Hello World"


#decorate = my_decorator(say_hello)
print(say_hello())
