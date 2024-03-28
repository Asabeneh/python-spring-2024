# What is the world's population
# create a json file that contains only country name, continent, capital and population

from fetch_data import fetch_data, create_json_file
from pprint import pprint


countries_url = 'https://restcountries.com/v3.1/all'
countries = fetch_data(countries_url)

populations = []
for country in countries:
    populations.append(country['population'])

print(populations)
total = sum(populations)
min_population = min(populations)
max_population = max(populations)
print(total, max_population, min_population)


lst_countrires  = []
for country in countries:
    name = country['name']['common']
    population = country['population']
    continents = country.get('continents')
    capital = country.get('capital')
    capital = capital[0] if capital else ''
    continent = continents[0] if continents else ''
    dct = {
        'name':name,
        'capital':capital,
        'population':population,
        'continent':continent
    }
    lst_countrires.append(dct)

# pprint(lst_countrires)

create_json_file('transformed-countries.json', lst_countrires)