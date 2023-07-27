# Data Structures in Python

# List: this is a collection of ordered data of varying types.
l1: list = list()

#print(dir(l1))   # Displays methods associated with data structure

# adding to a list/array
l1.append(3)
l1.append(-1)
l1.append(2)


# print(l1)

l1.sort() # to arrange elements in ascending order

# print(l1)

l1.sort(reverse=True) # to arrange in descending order

# print(l1)

l1.insert(0, 7)   # to add element in a given position

# print(l1)

l2: list = l1.copy()   # new list
# print("L2: ", l2)

# Is l1 equal to l2
# print(l1 == l2)

#  Empty the list
l1.clear()

# print(l1)

l3: list = [3, 4, 6, 'Kaleb', True]

#  Append vs Extend
l1.extend(l3)
# print(l1)

# Getting elements from list
# print("Zeroth Index: ", l1[0])

# Getting index of elements
# print(l1.index('Kaleb'))

# Negative Indexing in Python
# print(l1[-2])

# Slicing & Striding
names: list = ['Prevz', 'Kaleb', 'Divine', 'Koli', 'Henshaw']
# Slicing
# list_name[start:end]
print(names[1:4]) 

# Striding
#  list_name[start:end:step]
print(names[0:5:2])

del names   # purge completely from memory

try:
    print(names)
except NameError:
    print("names variable is not found in memory!")

# Simple Program

# First Class -> Scholarship -> 4.5 - 5.0
# Second Class Upper -> Continue Education -> 3.5 - 4.49
# Second Class Lower -> Rewrite Exams -> 2.5 - 3.49
# Third Class -> Fail -> 1.5 - 2.49

gpa_scores: list = [4.6, 4.53, 3.7, 1.5, 2.45, 1.0]

for score in gpa_scores:
    if (score >= 1.5) and (score <= 2.49):
        print(score, 'Failed!')
    elif (score >= 2.5) and (score <= 3.49):
        print(score, 'Rewrite Exams!')
    elif (score >= 3.5) and (score <= 4.49):
        print(score, 'Continue Education!')
    elif (score >= 4.5) and (score <= 5.0):
        print(score, 'Scholarship!')
    else:
        print(score, 'Change Program Sharp!')


# Project: Try a Rock-Paper-Scissors Game... Till next class on Wednesday!