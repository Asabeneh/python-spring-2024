# what is a module 

""" import math

print(dir(math))
print(math.pi)

pi = math.pi
print(math.sqrt(9))
print(math.sqrt(2))

print(round(9.81))
print(round(3.14))
print(math.floor(9.81))
print(math.floor(3.14))
print(math.ceil(3.14))
print(math.tau)
print(2 ** 3)
print(math.pow(2, 3))
print(math.log10(1000))
print(math.factorial(5)) # 5 * 4 * 3 * 2 * 1 """

""" 
from math import pi, sqrt, floor, ceil, pow, log10, factorial, tau

pi = pi
print(sqrt(9))
print(sqrt(2))

print(round(9.81))
print(round(3.14))
print(floor(9.81))
print(floor(3.14))
print(ceil(3.14))
print(tau)
print(2 ** 3)
print(pow(2, 3))
print(log10(1000))
print(factorial(5)) # 5 * 4 * 3 * 2 * 1 """



""" from math import pi, sqrt as square_root, floor, ceil, pow, log10, factorial as f, tau

pi = pi
print(square_root(9))
print(square_root(2))

print(round(9.81))
print(round(3.14))
print(floor(9.81))
print(floor(3.14))
print(ceil(3.14))
print(tau)
print(2 ** 3)
print(pow(2, 3))
print(log10(1000))
print(f(5)) # 5 * 4 * 3 * 2 * 1 """


from math import  *
pi = pi
print(sqrt(9))
print(sqrt(2))

print(round(9.81))
print(round(3.14))
print(floor(9.81))
print(floor(3.14))
print(ceil(3.14))
print(tau)
print(2 ** 3)
print(pow(2, 3))
print(log10(1000))
print(factorial(5)) # 5 * 4 * 3 * 2 * 1

import random
print(dir(random))
print(random.random()) # 0 to 0.999999999999999999
# write a script that generate 4 random numbers between 0 and 10

lottor = []

for i in range(7):
    value = floor(random.random() * 11)
    lottor.append(value)

print(lottor)

letters_numbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'

# Generate random user id of 6 characters



def generate_user_id(n = 6):
    id = ''
    for i in range(n):
        value = random.choice(letters_numbers)
        id += value
    return id


user_id = generate_user_id(64)
print(user_id)
fruits = ['banana','apple','lemon']
random.shuffle(fruits)
print(fruits)

from custom_modules import make_square, sum_all_nums, change_list_items_to_upper as change_to_upper
from countries import countries


print(make_square(5))
print(sum_all_nums([5, 10, 15, -30]))
print(change_to_upper(countries))

""" 
import os 
import math
import random
----
"""

""" 
To export it to a different location,  the folder should have __init__.py file without anything

"""