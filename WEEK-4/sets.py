# we will learn about set
# what is purpose - this is useful to remove duplicates
s = {1, 2, 2, 3, 4, 4}
print(s)
print(len(s))
print(type(s))

s.add(5)
print(s)
s.update((6, 7,8,9))

print(s)
s.remove(7)
print(s)
# s.clear()
# print(s)
lst = list(s)
print(lst)

# A, B, AUB, AnB, A\B, B\A, AdeltaB
A = {1, 2, 3, 4, 5, 6} # AUB => {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {2, 3, 4, 7, 8, 9} # AnB = {2, 3, 4}
# A\B = {1, 5, 6}
# B\A = {7, 8, 9}
# (A\B) U (B\A) = {1, 5, 6, 7, 8, 9}

print('AUB = ', A.union(B))
print('AnB = ', A.intersection(B))
print('A\B = ', A.difference(B))
print('B\A = ', B.difference(A))
print('(A\B) U (B\A) = ', A.symmetric_difference(B))
print(A.issuperset(B))
print(A.isdisjoint(B))

sentence = 'I love teaching and their nothing like teaching. Becuase of the love of teaching. I will teach all the time. Do you love teaching? What do you love? Love is a great thing to have.'

# Numbers of words
# Number of unique words
# Lexical variety of sentence

words = sentence.lower().strip().replace('.', '').replace('?', '').split()
print(words, len(words))
total_words = len(words)
unique_words = set(words)
total_unique_words = len(unique_words)
print(unique_words, len(unique_words))
print(round(total_unique_words / total_words * 100, 1))

fruits = {'banana', 'orange', 'mango', 'lemon', 'Papaya'}
fruits.discard('Papaya')
print(fruits)
