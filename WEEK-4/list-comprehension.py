# List comprehension - Instead of using regular loop we use list comprehension - it takes less memory, high performant and clean code
from countries import countries
nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

""" new_nums = []

for num in nums:
    new_nums.append(num * 2)

print(new_nums) """

new_nums = list(map(lambda num: num * 2, nums))
print(new_nums)

# List comprehension

new_lst = [num * 2  for num in nums]

countries_uppercased = [country.upper() for country in countries]
print(countries_uppercased)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([n  for nums in lst for n in nums])

print([country.upper() for country in countries if 'land' in country])

def find_country_by_substring(term):
    lst = [country for country in countries if  term in country]
    numbers = len(lst)
    return lst, numbers

print(find_country_by_substring('stan'))

