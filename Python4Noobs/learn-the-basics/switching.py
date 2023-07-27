# An alternative to if-else statements in Python is Switch-Case

# Syntax:

# match term:
#     case pattern-1:
#         action-1
#     case pattern-2:
#         action-2
#     case pattern-3:
#         action-3
#     case _:
#         action-default

# N/B: The underscore symbol (_) is what you use to define a default case for the switch-case statement in Python

# Sample Program: This is a program that prints what you can become when you learn various programming languages

lang: str = input("What's the programming language you want to learn? - \t")

match lang:
    case 'Javascript': print('Full-Stack Web Developer!')
    case 'Python': print('Data Scientist!')
    case 'PHP': print('Backend Web Developer!')
    case 'Solidity': print('Blockchain Developer!')
    case 'Java': print('Mobile App Developer!')
    case _: print('The language does not matter. What matters is problem solving!')
