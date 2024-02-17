""" 
if 
if else 

if elif elif else

"""
a = 10
print(a > 0)
if a > 0:
    print(f'{a} is a postive number')
elif a < 0:
    print(f'{a} is a negative number')
else:
   print(f'{a} is zero')
   
   
num = -10

if num >= 0:
    print(f'The absolute value of {num} is {num}')
else:
    print(f'The absolute value of {num} is {-1 * num}')
    
is_raining = False 

if is_raining:
    print('Go with an umbrella')
else:
    print('Go out freely')


weather = input('Enter the todays weather: ').lower()

if weather == 'rainy':
    print('Go with an umbrella') 
elif weather == 'cloudy':
    print('There might be rain')
elif weather == 'sunny':
    print('It is such a shinny day')
elif weather == 'snowy':
    print('It might be slippery')
elif weather == 'foggy':
    print('There might be visibility problem')
else:
    print('No knows about the weather')
    
first_name = 'Asabeneh'
value = 'Your name is too long' if len(first_name) > 5 else 'You have got a short name'
print(value)
