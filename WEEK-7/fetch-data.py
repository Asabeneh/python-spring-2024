# We fetch data from the internet: API, website
import requests
from pprint import pprint
quote_url = 'https://api.quotable.io/random'

# Requests: GET, POST, PUT, DELETE
def fetch_data(url):
    response = requests.get(url)
    if url.endswith('.txt'):
        return response.content
    else:
        data = response.json()
        return data

pprint(fetch_data(quote_url))


url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

print(fetch_data(url))
countries_url = 'https://restcountries.com/v3.1/all'
countries = fetch_data(countries_url)
""" for country in countries:
    #  country['languages'],
    print(country['population'], country.get('subregion'), country['name']['common'], country['name']['official'], country['continents'], country.get('capital')) """

cats = fetch_data('https://api.thecatapi.com/v1/breeds')

for cat in cats:
    pprint(cat)


# What is the world's population
# create a json file that contains only country name, continent, capital and population