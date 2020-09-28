# Module for division
def Division(num1, num2):
    try:
        resullt = num1 / num2
        return resullt
    except ZeroDivisionError:
        print("Division by zero not possible")