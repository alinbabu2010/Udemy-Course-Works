# Calculator program in Python
from operations import add,sub,div,multi

while(1):
    try:
        choice = int(input("Enter your choice of operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5.Exit\n"))
    except ValueError:
        print("Enter a valid choice.")
    
    if (choice == 5):
        print("Bye!\n")
        break;
    elif (choice > 5):
        print("Enter a valid choice.")
        continue

    try:
        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
    except ValueError:
        print("Enter a valid number. No other inputs\n")
        continue

    if (choice == 1):
        result = add.Addition(num1, num2)
    elif (choice == 2):
        result = sub.Subtraction(num1, num2)
    elif (choice == 3):
       result = multi.Multiplication(num1, num2)
    elif (choice == 4):
        result = div.Division(num1, num2)
    
    
    if (result):
        print("Result = ", result)
    