# List : index, order, mutable
# Set: no order, no indexing, does allow duplicates, mutable
# Dictionary: key and value pair, mutable
# Tuple: index, order, immutable

tp = tuple()
print(type(tp))

tp = (1, 2, 3, 4, 2, 4, 5)
print(tp.count(2))
print(len(tp))
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits_lst = list(fruits)
fruits_lst.append('Papaya')
print(fruits_lst)

print('lemon' in fruits)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)