# snake_case when we were declaring variables and functions
# oop: we use CamelCase

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed 
        self.age = age 
        self.color = color
    def get_dog_info(self):
        return f'Here is the dog\'s info:The breed is {self.breed}, the age is: {self.age}, the color:{self.color}'


d1 = Dog('Husky', 5, 'brown')
print(d1.breed)
print(d1.age)
print(d1.color)
print(d1.get_dog_info())

class Person:
    def __init__(self, first_name, last_name, city, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.age = age
        self.places = []
    def get_fullname (self):
        return self.first_name + ' ' +  self.last_name
    def get_person_info(self):
        full_name = self.get_fullname()
        places = ', '. join(self.places)
        return f'He is {full_name}. He is {self.age} years old. He lives in {self.city}, {self.country}. He has visited {len(self.places)} places such as {places}'
    def add_place(self, place):
        self.places.append(place)

print(Person)

p1 = Person('Asabeneh','Yetayeh','Finland','Helsinki', 250)
print(p1)
print(p1.first_name)
print(p1.last_name)
print(p1.country)
print(p1.get_fullname())

p1.add_place('Estonia')
p1.add_place('Finland')
p1.add_place('Sweden')
p1.add_place('Denmark')
p1.add_place('Norway')

print(p1.places)

print(p1.get_person_info())


""" 
p2 = Person('John','Doe','Sweden','Stockholm', 21)
print(p2.first_name)
print(p2.last_name)
print(p2.country)
print(p2.get_fullname())

p2.add_place('Thailand')
p2.add_place('Egypt')
p2.add_place('China')
p2.add_place('Japan')
p2.add_place('Korea')

print(p2.places)

print(p2.get_person_info())


p2 = Person('Melisa','Robert','United Kingdom','London', 24)
print(p2.first_name)
print(p2.last_name)
print(p2.country)
print(p2.get_fullname())

p2.add_place('Finland')
p2.add_place('Egypt')
p2.add_place('Algeria')
p2.add_place('Japan')
p2.add_place('Korea')

print(p2.places)

print(p2.get_person_info()) """

class Student(Person):
    def __init__(self, first_name, last_name, country, city, age, gender):
        super().__init__(first_name, last_name, country, city, age)
        self.gender = gender
        self.skills = []
        self.points = 0
    def get_person_info(self):
        full_name = self.get_fullname()
        places = ', '. join(self.places)
        pronoun = 'He' if self.gender == 'Male' else 'She'
        visited_places =  '' if len(self.places) == 0 else f'{pronoun} has visited {len(self.places)} places such as {places}'
        return f'{pronoun} is {full_name}. {pronoun} is {self.age} years old. {pronoun} lives in {self.city}, {self.country}. {visited_places}'
    
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills(self):
        return ', '.join(self.skills)
    def add_point(self):
        self.points += 5


s1 = Student('James', 'Robert', 'United Kingdom', 'London', 25, 'Male')
print(s1.get_person_info())
s1.add_skill('Python')
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('MySQL')
print(s1.get_skills())

s1 = Student('Lidiya', 'Teklemariam', 'Finland', 'Helsinki', 28, 'Female')
print(s1.get_person_info())
s1.add_skill('Git and GitHub')
s1.add_skill('HTML')
s1.add_skill('CSS')
s1.add_skill('MySQL')
print(s1.get_skills())
s1.add_point()
print(s1.points)
