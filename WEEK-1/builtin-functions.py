"""
This script demonstrates the usage of various built-in functions in Python.

Functions covered:
- print(): Displays the given arguments when executed.
- len(): Returns the number of elements in a sequence (strings, lists, sets, tuples, dictionaries).
- type(): Returns the type of the specified object.
- min(): Returns the smallest item in a sequence.
- max(): Returns the largest item in a sequence.
- sum(): Returns the sum of all items in a sequence.
- int(): Converts a specified value to an integer.
- float(): Converts a specified value to a floating-point number.
- str(): Converts a specified value to a string.
- range(): Generates a sequence of numbers with specified start, stop, and step values.
- list(): Converts a sequence to a list.

Author: Asabeneh Yetayeh
Date: February 7 2024
"""

# Demonstrating the print function with various arguments
print('Hello world!')
print('Hello', 'world!')
print('Helllo', 'world', '!')
print('line 1', end='')
print('line 2')

# Demonstrating the len function with strings and lists
print('Python')
print(len('Python'))
print(len([1, 2, 3, 4, 5]))

# Demonstrating the type function with different data types
print(type(10))
print(type(3.14))
print(type('Python'))
print(type([1, 2, 3]))

# Demonstrating the min, max, and sum functions
print(min(1, 2, 3, 10, -100, 0))
print(max(1, 2, 3, 10, -100, 0))
print(sum([1, 2, 3, 10, -100, 0]))

# Demonstrating conversion functions
print(4 == '4')
print(4 == int('4'))
print(str(4) == '4')

g = '9.81'
print(float(g) + 0.19)
print(int(float(g)))

# Demonstrating the range function and converting it to a list
print(range(1, 6, 1))
r = range(101)
print(list(r))
evens = range(0, 101, 2)
print(list(evens))
odds = range(1, 101, 2)
print(list(odds))

# creating a list from a string using list() function

letters = list('Python') 

# Commented out user input for better code execution in a script
# year = int(input('year born: '))
# age = 2024 - year
# print(age)

# Displaying the list of attributes for an empty list
print(dir([]))
