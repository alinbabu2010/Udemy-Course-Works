# Implementing basic exception handling

x = 20
try:
    print(x)
except:
    print("Varible is not defined")
else:
    print("Hello")
finally:
    print("You may get an error if no variable is specified")


'''b = "Hello"
print(int(b))'''

# Example of specific exceptiopn handling
while True:
    try:
        n = int(input("Enter a whole number\n"))
        break
    except ValueError:
        print("No valid integer entered.")

print("Great you have enterd an integer")

try:
    n = 12 / int(input("Enter a whole number\n"))
    print("The value of your number is ",n)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    pass
finally:
    print("Hope you enter a valid whole number.")