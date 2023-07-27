# Looping: This is the act of carrying out a particular task and within the principle and confines of programming, this is the act of carrying out a repetitive task for a certain number of times or until a condition is met or satisfied

fruits: list = ['apple', 'banana', 'cucumber', 'mango', 'strawberry', 'orange', 'olives', 'grapes', 'watermelon']

# For-Loop ----------------------------------------------------------------------------
for fruit in fruits: print(f'I love eating {fruit}')

# While-Loop ---------------------------------------------------------------------------
idx: int = 0

while (idx < len(fruits)):
    print(f'I love {fruits[idx]}')
    idx += 1   # shorthand version of writing: idx = idx + 1

#  The else part only works if there is no break statement in the for loop or while loop

# For-Else Loop -------------------------------------------------------------------------
for fruit in fruits: print(f'I love eating {fruit}')
else: print('Those are my favorite fruits.')

# While-Else Loop -----------------------------------------------------------------------
while (idx < len(fruits)):
    print(f'I love {fruits[idx]}')
    idx += 1   # shorthand version of writing: idx = idx + 1
else: print('Those are my best fruits.')

# Control Statements --------------------------------------------------------------------

# 1. pass: do nothing -------------------------------------------------------------------
# Example
for fruit in fruits:
    pass

# 2. continue: go to the beginning of the loop but do nothing ---------------------------
# Example
numbers: list = list(range(1,11,1))
# Using continue to print only odd numbers from the numbers list
for number in numbers:
    if (number % 2 == 1): print(num)
    else: continue    

# 3. break: stop the iteration of both the for and while loop ---------------------------
# Example
# Using break to print only the first five numbers from the numbers list
for number in numbers:
    if (number == 6): break
    else: print(number)
# -----------------------------------------------------------------------------------------