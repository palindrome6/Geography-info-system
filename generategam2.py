import pycountry
import pystache
import json
from slugify import slugify

with open('neighbors.json') as neighbor_data_file:
	neighbor_data = json.load(neighbor_data_file)

def get_country_title_by_code(code):
	return pycountry.countries.get(alpha2=code).name.encode('ascii', 'ignore').decode('ascii')

def get_neighbors(code):
	return [slugify(neighbor) for neighbor in neighbor_data[code] if neighbor in concept_names]

def map_concept(concept, level, parent):
	country = level is '3'
	title = get_country_title_by_code(concept) if country else concept
	return {
		'title': title,
		'level': level,
		'name': slugify(concept),
		'filename': slugify(concept, separator='_'),
		'parent': slugify(parent) if parent is not None else None,
		'country': country,
		'neighbors': get_neighbors(concept) if country else []
	};

with open('countrylist.txt', 'r') as country_file:
	
	concepts = []
	parents = {}
	
	raw_concept_data = country_file.read().splitlines()
	all_concept_data = [data.split(',') for data in raw_concept_data]
	
	concept_names = [concept_data[0] for concept_data in all_concept_data]

	for (concept, level) in all_concept_data:
		parents[level] = concept
		parent_level = str(int(level) - 1)
		parent = parents[parent_level] if parent_level in parents else None
		concepts.append(map_concept(concept, level, parent))

	with open('concepts.mustache', 'r') as template_file:
		with open('concepts.gam', 'w') as concepts_file:
			renderer = pystache.Renderer(escape=lambda u: u)
			
			concepts_file.write(renderer.render(template_file.read(), {
				'concepts': concepts
			}))
