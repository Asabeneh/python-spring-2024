# the term its is explanatory: 
# it is a list of something: a list some data type

empty_list = []
print(empty_list)
print(len(empty_list))
print(type(empty_list))

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num, num * 100)
    


lst = ['Asab', 250, True, ['HTML','JS','Python']]

# Manipulate the list
# list is an ordered and indexed
shopping_list = ['Milk', 'Potatoes', 'Coffee','Tea', 'Sugar']
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4])

length = len(shopping_list)
last_index = length - 1
print(shopping_list[last_index])
print(shopping_list[:])
print(shopping_list[0:])
print(shopping_list[2:4])
beverages = shopping_list[2:4]
print(beverages)
print(shopping_list[3:])
print(shopping_list[3:5])

print(shopping_list[-1])
print(shopping_list[-2])
print(shopping_list[-3])
print(shopping_list[-5])
print(shopping_list[-3:-1])
print(shopping_list[-4:])

shopping_list.append('Meat')

print(shopping_list)
shopping_list[4] = 'Honey'

print(shopping_list)
shopping_list[0] = 'Cheese'
print(shopping_list)

shopping_list.insert(2, 'Tomatoes')
print(shopping_list)

# shopping_list.remove('Coffee')

print(shopping_list)

print('Milk' in shopping_list)

# for item in shopping_list:
#     print(item)
    
del shopping_list[3:5] 
print(shopping_list)
# shopping_list.clear()
print(shopping_list)

num1 = [1, 2, 3]
num2 = [4, 5, 6]
print(num1 + num2)
num2.extend(num1)

shopping_list.extend(['Apple','Papaya','Avacodo','Guava'])
print(shopping_list)

nums = [1, 2, 2, 3, 4, 5, 4, 5, 3, 3, 3, 3, 2, 10]
print(nums.count(3))
print(nums.index(1))
nums.reverse()

print(nums)

students = ['Alexandra', 'Elena', 'Jeremys','Max', 'Niken','Stais','Manca','Motiur','Armand','Simone','Irina','Kristina']

students_copy = students.copy()
students_copy.sort()

print(students)
print(students_copy)

print(sorted(students))
print(students)

new_students = []
for student in students:
    new_students.append(student.upper())
    
print(new_students)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

new_countries = []
for country in countries:
    # new_countries.append([country, len(country), country.upper(), country.upper()[0:3]])
     new_countries.append([country, country.upper()[0:3]])
print(new_countries)

countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)


