import pycountry
import pystache
from slugify import slugify

def get_country_title_by_code(code):
	return pycountry.countries.get(alpha2=code).name.encode('ascii', 'ignore').decode('ascii')

def map_concept(concept, level, parent):
	country = level is '3'
	title = get_country_title_by_code(concept) if country else concept
	return {
		'title': title,
		'level': level,
		'name': slugify(concept),
		'filename': slugify(concept, separator='_'),
		'parent': slugify(parent) if parent is not None else None,
		'country': country
	};

with open('countrylist.txt', 'r') as country_file:
	
	concepts = []
	parents = {}

	for concept_data in country_file.read().splitlines():
		(concept, level) = concept_data.split(',')
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
