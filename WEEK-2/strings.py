# most data is in the form  of text
# messasge, tweets, linkedin post, blog post any thing you may imagine

# How to create a variable: single, double, triple quote
# A string could a single character or multiple pages
#What is the difference between a bultin function and a method

letter = 'A'
print(letter)
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(letters)
print(len(letters))
print(letters.lower())
print(letters.upper())

sentence = 'Python for everyone'

print(sentence.lower())
print(sentence.title())
print(sentence.swapcase())
words = sentence.split()
print(words, len(words))
print(sentence.count('e'))

dna = """CGTGGGCGGCCACTGGTGAGTTACTACACCCCAGGGGCAACGTTGATGCTCCTAAAAAACTCTGGCTGGACGCAAGCCGTAACACCCGTGTCACTTCATAATCGTTTGCAATTCAGGGCTTGATCTACACTGGATTGCCATTCTCTCAAAGTATTATGCAGGACGGCGTGCGCGTTCCATGTAAACCTGTCATAACTTACCTGAGACTAGTTGGAAGTGTGGCTAGATCTTTGCTCACGCATCTAGTCGGTCCACGTTTGGTTTTTAAGATCCAATGATCTTCAAAACGCTGCAAGATTCTCAACCTGCTTTACTAAGCGCTGGGTCCTACTCCAGCGGGATTTTTTATCTAAAGACGATGAGAGGAGTATTCGTCAGACCACATAGCTTTCATGTCCTGATCGGAAGGATCGTTGGCGCCCGACCCTCAGACTCTGTAGTGAGTTCTATGTCCGAGCCATTGCATGCGAGATCGGTAGATTGATAGGGGATACAGAATATCCCTGGATGCAATAGACGGACAGCTTGGTATCCTAAGCGTAGTCGCGCGTCCGAACCCAGCTCTACTTTAGAGGCCTCGGATTCTGGTGCCCGCAGGCCGCAGAACCGATTAGGGGCATGTACAACAATATTTATTAGTCACCTTTGAGACACGATCTCCCACCTCACTGGAATTTAGTTCCTGCTATAATTAGCCTTCCTCATAAGTTGCATTACTTCAGCGTCCCAACTGCACCCTTACCACGAAGACAGGTTTGTCCATTCCCATACTGCGGCGTTGGCAGGGGGTTCGCATGTCCCACGCGAAACGTTGCTGAAGGCTCAGGTTTCTGAGCGACAAAAGCTTTAAACGCGAGTTCCCGCTCATAACTTGGTCCGAATGCGGGTTCTTGCATCGTTCCACTGAGTTTGTTTCATGTAGGACGGGCGCAAAGTATACTTAGTTCAATCTTCAATACCTTGTATTATTGTACACCTACCGGTCACCAGCCAACAATGT"""
print(len(dna))

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')
print('A', A,  'C:', C, 'G:', G,'T:', T)

# string concatenation:
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' +  last_name 
print(full_name)
print('4' + '4')
# new line
print('I am Asabeneh. \nI love teaching.\nTeaching Python is the most interesting thing.')

# tab

print('''To became a machine learning specialist you need the following skills:
      \t- Python
      \t- Mathematics(Statistics)
      \t- Database
      ''')

print("I don't like to use double quote instead I prefer single quote")
print('I don\'t like to use double quote instead I prefer single quote')
print('People used to say "An apple a day keep the doctor away"')
print("People used to say \"An apple a day keep the doctor away\"")
print('It is hard to be 100 % efficient.')
print('Is is possible to print \\ in latest Python')

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
age = 250
height = 1.73
formated_string = 'I am %s %s. I teach %s. I am %d. I am %.2f.' %(first_name, last_name, language, age, height)
print(formated_string)

# New Style String Formatting (str.format)

''' 
I am Asabeneh Yetayeh. I am fullstack developer, based in Helsinki, Finland. I am 250 years old.
'''

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
position = 'Fullstack'
language = 'Python'
age = 250
height = 1.73

print('I am {} {}. I am {} developer, based in {}, {}. I am {} years old.'.format(first_name, last_name, position, city, country, age))

a = 4 
b = 3 
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} x {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ^ {} = {}'.format(a, b, a ** b))


# String Interpolation / f-Strings (Python 3.6+)
print(f'I am {first_name} {last_name}. I am {position} developer, based in {city}, {country}. I am {age} years old.')

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = { a - b}')
print(f'{a} x {b} = { a * b}')
print(f'{a} / {b} = { a / b}')
print(f'{a} % {b} = { a % b}')
print(f'{a} // {b} = { a // b}')
print(f'{a} ^ {b} = { a ** b}')
print('Python'[2])

language = 'Python'
print(language[0])
print(language[1])
print(language[5])
last_index = len(language) - 1
print(language[last_index])
print(language[2:])

print(language[-1])
print(language[-2])
print(language[::-1])

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
# String methods
country = 'Finland'
print(country.endswith('d'))
print(country.startswith('Fin'))
print(country.startswith('F'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs(25))
print(len('                     '))

challenge = 'thirty days of python'

print(challenge.find('the'))
print(challenge.rfind('th'))

print(challenge.index('th'))
print(challenge.rindex('th'))

word = 'abc123'
print(word.isalpha())

variable = '11first_name'
print(variable.isidentifier())
print('BOOK'.isupper())
print('BOOK'.islower())

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ', '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

challenge = 'thirty days of python'
print(challenge)
print(challenge.strip('on')) #

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

print('I like people because people are great.'.replace('like', 'love').replace('people','animals'))
txt  = 'I like people because people are great.'.replace('like', 'love').replace('people','animals')
print(txt)
words = txt.split()
print(words)
print(txt.split('because'))