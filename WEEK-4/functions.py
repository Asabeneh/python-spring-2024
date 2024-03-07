# Functions - block of code that perform a certain task
# Functions can be reused
# Functions make our code clearn, readable, maintainable, and testable


# Different builtin functions: print, len, abs, str, input, float, dir, round, list, tuple, dict, etc to perform a certain taks
# We will write our custom function

def do_something ():
    print('I am teaching Python right now.') 
    
    
do_something()

def greetings(city):
    print(f'Hello world! We are greeting the world from the beautiful {city}')
    
greetings('Helsinki')
greetings('Stockholm')
greetings('Oslo')
greetings('Copenhagen')

def add_two_nums(a, b):
    total = a + b
    return total
    
    
print(add_two_nums(1, 2))
print(add_two_nums(99, -99))
print(add_two_nums(1, 99))

def print_fullname (first_name, last_name):
    return f'{first_name} {last_name}'

print(print_fullname('Asab','Yeta'))
print(print_fullname('Donlad ','Trump'))


""" def sum_all_nums(n):
    total = 0
    for i in range(n + 1):
        total = total + i
        
    return total

print(sum_all_nums(2))
print(sum_all_nums(10))
print(sum_all_nums(100)) """
    

def sum_all_nums(n):
    total = sum(range(n + 1))
    return total

print(sum_all_nums(2))
print(sum_all_nums(10))
print(sum_all_nums(100))


def reverse_list (lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

lst = [1, 2, 3, 4]
print(reverse_list(lst))
students = ['Alexandra', 'Elena', 'Jeremys','Max', 'Niken','Stais','Manca','Motiur','Armand','Simone','Irina','Kristina']
print(reverse_list(students))

# Calcuate the weight of  a body in different gravity 
# mass 75 kg, 9.81 
# calculate_weight ? mass * gravity
# Earth: 9.81, Jupiter: 24.79  Mercury: 37, Moon: 1.62

def calculate_weight(mass, gravity = 9.81):
    weight = mass * gravity 
    return weight

print(calculate_weight(75))
print(calculate_weight(75, 24.79))
print(round(calculate_weight(75, 1.62), 2))
print(round(calculate_weight(85)))

def make_square(n):
    return n ** 2

print(make_square(10))
print(make_square(7))

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_full_name(lastname='Yetayeh', firstname='Asabeneh'))
print(print_full_name(firstname='Asabeneh', lastname='Yetayeh'))
# Arbitary number of arguments

def sum_all_nums(*args):
    return sum(args)

print(sum_all_nums(1, 2, 3, 4, 5, 6, 79, 900, -500))

def funct_with_kwargs(**kwargs):
    
    for key in kwargs:
        print(key, kwargs[key])
    
    
    
    
print(funct_with_kwargs(first_name = 'Asab', last_name = 'Yetayeh', age = 250, skills = ['HTML', 'Python', 'Node.js']))