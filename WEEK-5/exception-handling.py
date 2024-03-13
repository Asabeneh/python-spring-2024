""" 
try:
    user = {}
    print(user['age'])
except TypeError:
    print('Type error')
except ValueError:
    print('value error')
except ZeroDivisionError:
    print('zero division error')
except KeyError:
    print('Key error')
finally:
    print('slslsll this block will be printed all the time') """



try:
    user = { 'name':'Asb'}
    # print([1, 2, 3][3])
    print(user['age'])
except Exception as e:
    print(e)
finally:
    print('slslsll this block will be printed all the time')