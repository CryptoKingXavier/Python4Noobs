# Casting is simply type conversion: the act of converting from one data type to another

# Str -> Int
age: str = '15'
new_age: int = int(age)

# Str -> Float
my_new_age: float = float(age)

# print(type(age), age)
# print(type(new_age), new_age)
# print(type(my_new_age), my_new_age)

# Bool -> Int
isOnline: bool = True
isMarried: bool = False

print(int(isOnline))
print(int(isMarried))

# Bool -> Float
print(float(isOnline))
print(float(isMarried))