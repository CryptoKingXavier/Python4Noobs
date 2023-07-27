# Exceptions are simply Python's Representation of Errors

# Exception Handling
# 1. try ... except ...
# 2. try ... except ... finally

# ZeroDivisionError: This occurs when dividing by 0
# Using try ... except ...
def Divide(num1: float, num2: float) -> None:
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('Undefined!')


# Using try ... except ... finally ...
def Divide(num1: float, num2: float) -> None:
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('Undefined!')
    finally:
        print('Thanks 4 Using My Program!')

Divide(3, 0)
