# Python Programming

## Hello World in Python

### Print Statements in Python

This script demonstrates basic usage of print statements in Python.

## Usage

- Run the script to see the output of various print statements.

**Author:** Asabeneh Yetayeh  
**Date:** February 7, 2024

```python
# Demonstrate different ways to create strings

# Print a simple greeting
print('Hello world!')

print('Do you love Python?')

print('I really really love Python')

print("We can create a string using a single quote, double quote, or multiple quotes")

print('''It is possible to make a string with triple quote''')

print("""It is possible to make a string using triple quotes""")
```

## Python Operators Usage

This script demonstrates the usage of various operators in Python.

**Operators:**

- Assignment operators (`=`)
- Arithmetic operators (`+`, `-`, `*`, `/`, `%`, `//`, `**`)
- Comparison operators (`>`, `>=`, `<`, `<=`, `==`, `!=`, `is`, `is not`, `in`, `not in`)
- Logical operators (`and`, `or`, `not`)

## Arithmetic operators

```python
print('The addition of 4 and 3 is', 4 + 3)
print('The subtraction of 4 and 3 is', 4 - 3)
print('The product of 4 and 3 is', 4 * 3)
print('The division of 4 and 3 is', 4 / 3)
print('The remainder of 4 divided by 3 is', 4 % 3)
print('The floor division of 4 and 3 is', 4 // 3)
print('4 raised to the power of 3 is', 4 ** 3)
```

## Variables and assignment operators

```py
a = 4
b = 3
c = a + b
print(a)
print(b)
print(c)
```

## Comparison operators

```py
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
```

## Logical operators

```py
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
```

## Python Data Types

This script provides examples and explanations for various data types in Python.

**Data types covered:**

- **String:** Represents text and can be created using single, double, or triple quotes.
- **Numbers:** Includes integers, floating-point numbers, and complex numbers.
- **Boolean:** Represents true or false values.
- **List:** An ordered collection of items.
- **Tuple:** An ordered, immutable collection of items.
- **Set:** An unordered collection of unique items.
- **Dictionary:** A collection of key-value pairs.

```python
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
```

## Numbers data type

- Numbers include integers, floating-point numbers, and complex numbers.

```py
a = 4
print(a, type(a))

pi = 3.14
print(pi, type(pi))

c = 1 + 2j
print(c, type(c))
```

## Boolean data type

- Represents true or false values.
- Used in logical operations.

```py
print(print(type(True)))
print(print(type(False)))
```

## List data type

- An ordered collection of items.

```py
nums = [1, 2, 3, 4, 5]
names = ['Asab', 'Eyob', 'Marta', 'John']
```

## Tuple data type

- An ordered, immutable collection of items.

```py
nums_tuple = (1, 2, 3, 4, 5)
```

## Set data type

- An unordered collection of unique items.

```py
nums_set = {1, 2, 3, 4, 5}
```

## Dictionary data type

- A collection of key-value pairs.

```py
fin_en = {
    'sana': 'word',
    'talo': 'house',
    'kirja': 'book'
}
```
