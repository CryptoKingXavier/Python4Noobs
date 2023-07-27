# Variables

#variableName = value
# name = 'Alex'

#variableName: str = value
# String
name: str = 'Alex'
myName:str = "Alex"

# Numbers
# Integer
num1: int = 5

# Float
num2: float = 5.5

# Complex
#3 + 4i
num3: complex = complex(3, 4)

# Boolean: True or False
isMarried: bool = False

# Conditionals
# if ... statement
if (isMarried):
    print("He is married!")

# if ... else ... statement
age: str = input('Enter Age: ')
# Type Casting
age: int = int(age)

# Long Way
if (age >= 18):
    print('Drink Responsibly!')
else:
    print('Too Young to Drink!')

# Shorthand Version
# variableName = True-Section if condition else False-Section
message: str = 'Drink Responsibly!' if age >= 18 else 'Too Young to Drink!'

print(message)

# Conditionals

# if ... else if ... else ... statement
myAge: int = int(input('Enter Age: '))

# 1-12: Kid
# 13-19: Teenager
# 20-70: Adult
# >=70: Old Age

# Enforcing that both conditions must be True, we use the logical "and" keyword
if (myAge >= 1) and (myAge <= 12):
    print("You're still a kid!")
elif (myAge >= 13) and (myAge <= 19):
    print("You're a teenager awaiting adult life!")
elif (myAge >= 20) and (myAge <= 70): 
    print("Adulthood na scam!")
else:
    print('Welcome to the old life!')

# Creating constants in python
PI = 3.142

# User-Defied Functions
# Function Definition
def Sum(num1: float = 0, num2: float = 0) -> float:
    return num1 + num2

# Calling / Invoking the function
print(Sum(3, 4))
