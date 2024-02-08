"""
This script provides examples and explanations for various data types in Python.

Data types covered:
- String: Represents text and can be created using single, double, or triple quotes.
- Numbers: Includes integers, floating-point numbers, and complex numbers.
- Boolean: Represents true or false values.
- List: An ordered collection of items.
- Tuple: An ordered, immutable collection of items.
- Set: An unordered collection of unique items.
- Dictionary: A collection of key-value pairs.

Author: Asabeneh
Date: February 7, 2024
"""

# String data type
# - Strings can be created using single, double, or triple quotes.
# - They can represent a single character or multiple pages of text.
l = 'a'
print(len(l))

word = 'Python'
print(word)
print(len(word))

sentence = 'Everyone here loves to learn Python programming'
print(len(sentence))
print(sentence.split())
print(len(sentence.split()))

# Numbers data type
# - Numbers include integers, floating-point numbers, and complex numbers.
a = 4
print(a, type(a))

pi = 3.14
print(pi, type(pi))

c = 1 + 2j
print(c, type(c))

# Boolean data type
# - Represents true or false values.
# - Used in logical operations.
boolean_value = True
print(boolean_value, type(boolean_value))

# List data type
# - An ordered collection of items.
nums = [1, 2, 3, 4, 5]
names = ['Asab', 'Eyob', 'Marta', 'John']

# Tuple data type
# - An ordered, immutable collection of items.
nums_tuple = (1, 2, 3, 4, 5)

# Set data type
# - An unordered collection of unique items.
nums_set = {1, 2, 3, 4, 5}

# Dictionary data type
# - A collection of key-value pairs.
fin_en = {
    'sana': 'word',
    'talo': 'house',
    'kirja': 'book'
}
