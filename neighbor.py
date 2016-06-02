import json
import requests
from tqdm import tqdm

def find_neighbors(code):
    url = 'http://api.geonames.org/neighboursJSON'
    params = {
        'country': country['countryCode'],
        'username': 'jeroennoten'
    }
    response = requests.get(url=url, params=params)
    data = json.loads(response.text)
    if ('geonames' not in data):
        return []
    return [n['countryCode'] for n in data['geonames']]
        
countries = json.load(open('countries.json'))['geonames']
neighbors = {}
for country in tqdm(countries):
    neighbors[country['countryCode']] = find_neighbors(country['countryCode'])
    
with open('neighbors.json', 'w') as outfile:
    json.dump(neighbors, outfile)