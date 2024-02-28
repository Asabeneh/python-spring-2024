# key value data structure

dct = {}
print(type(dct))

user = {
    'email':'asab@asab.com',
    'username':'asab',
    'password':'123123'
}

for key in user:
    print(key, user[key])
    
    
person = {
    'first_name':'Asab',
    'last_name':'Yeta',
    'age':250,
    'skills':['HTML','CSS','JS','Python','Node','MYSQL'],
    'country':'Finland',
    'is_married':True,
    'address':{
        'street_name':'Space street',
        'zipcode':'02700'
    },
    'hobby':['Hikking','Mountain Climbing']
}

print(len(person))
print(person['first_name'])
print(person['last_name'])
skills = person['skills']
print(len(skills))
print(person.get('nationality'))
person['nationality'] ='Ethiopian'

print(person)
person['skills'].append('PostgreSQL')
print(person)

if 'hobby' in person:
    print(person['hobby'])
    
person['age'] = 60

print(person)

keys = person.keys()
values = person.values()

print(keys, values)
print(person.items())

for item in person.items():
    print(item[0], item[1])

person.pop('age')

print(person)
del person['hobby']

print(person)