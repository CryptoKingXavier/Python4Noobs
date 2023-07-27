# Calculator Application in Python

# Method 1
# Addition
def getSum(num1: float, num2: float) -> float: return num1 + num2

# Subtraction
def getDifference(num1: float, num2: float) -> float: return num1 - num2

# Multiplication
def getProduct(num1: float, num2: float) -> float: return num1 * num2

# Division
def getQuotient(num1: float, num2: float) -> float: return num1 / num2

# Operator
def getOperator(operator: str) -> float:
    num1: float = float(input('Number 1: '))
    num2: float = float(input('Number 2: '))

    if operator == '+': print('Sum = ', getSum(num1, num2))
    if operator == '-': print('Difference = ', getDifference(num1, num2))
    if operator == '*': print('Product = ', getProduct(num1, num2))
    if operator == '/': print('Quotient = ', getQuotient(num1, num2))

# Operation Check
# operator: str = input('Enter + or - or * or /: ')
# getOperator(operator)

# Method 2
def evalCalc(operation: str): print(eval(operation))

# evalCalc('4 + 7')

# Method 3
# Using formatted strings
def evalCalc1(num1: float, num2: float, operator: str): print(eval(f'{num1} {operator} {num2}'))

evalCalc1(3, 5, '+')

# Method 4
# Using string format
def evalCalc2(num1: float, num2: float, operator: str): eval('{} {} {}'.format(num1, operator, num2))

# Test Section
