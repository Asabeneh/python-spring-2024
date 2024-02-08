"""
This script demonstrates the usage of various operators in Python.

Operators:
- Assignment operators (=)
- Arithmetic operators (+, -, *, /, %, //, **)
- Comparison operators (> , >=, <, <=, ==, !=, is, is not, in, not in)
- Logical operators (and, or, not)

Author: Asabeneh Yetayeh
Date: February 7, 2024
"""

# Arithmetic operators
print('The addition of 4 and 3 is', 4 + 3)
print('The subtraction of 4 and 3 is', 4 - 3)
print('The product of 4 and 3 is', 4 * 3)
print('The division of 4 and 3 is', 4 / 3)
print('The remainder of 4 divided by 3 is', 4 % 3)
print('The floor division of 4 and 3 is', 4 // 3)
print('4 raised to the power of 3 is', 4 ** 3)

# Variables and assignment operators
a = 4
b = 3
c = a + b
print(a)
print(b)
print(c)

# Comparison operators
print(4 > 3)
print(4 >= 4)
print(4 >= 3)
print(4 < 3)
print(4 == 4)
print('The value here is', 4 != 4)
print(4 != '4')
print(4 == '4')
print(4 < 4)
print(4 is 4)
print(2 is not 4)
print(2 is not 2)
print('land' in 'Finland')
print('land' in 'Sweden')

# Logical operators
print(4 > 3 and 2 < 3)
print(4 < 3 and 2 < 3)

print(4 > 3 or 2 < 3)
print(4 < 3 or 2 < 3)
print(4 < 3 or 2 > 3)

print(not 4 > 3)
print(not not 4 > 3)

print('land' not in 'Finland')
print(not True)
print(not False)
