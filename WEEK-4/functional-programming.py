# map, filter, reduce

from countries import countries
from functools import reduce

nums = [1, 2, 3, 4] # [2, 4, 6, 8]
new_lst = []
def double ( n):
    return n * 2

for num in nums:
    new_lst.append(double(num))

print(new_lst)

doubled_nums = list(map(double, nums))
print(doubled_nums)
def change_to_upper(name):
    return name.upper()

students = ['Alexandra', 'Elena', 'Jeremys','Max', 'Niken','Stais','Manca','Motiur','Armand','Simone','Irina','Kristina']

print(list(map(change_to_upper, students)))
print(countries)


print(list(map(change_to_upper, countries)))

nums = [1, 2, 3, 4, 0, 5, -8, 2, 6, 10]

def filter_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
            
    return evens

print(filter_evens(nums))

def filter_odds(lst):
    odds = []
    for num in lst:
        if num % 2 != 0:
            odds.append(num)
            
    return odds

print(filter_odds(nums))

def filter_negative(lst):
    negative = []
    for num in lst:
        if num < 0:
            negative.append(num) 
    return negative

print(filter_negative(nums))

evens = list(filter(lambda num: num % 2 == 0, nums))
print(evens)

odds = list(filter(lambda num: num % 2 != 0, nums))
print(odds)

negatives = list(filter(lambda num: num < 0, nums))
print(negatives)

print(list(filter(lambda country: 'land' in country, countries)))
print(list(filter(lambda country: country.endswith('stan'), countries)))
print(list(filter(lambda country: country.startswith('S'), countries)))

def filter_country(key):
    return list(filter(lambda country: key in country, countries))

print(filter_country('Po'))    

print(reduce(lambda a, b: a + b, nums))