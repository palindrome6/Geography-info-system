import pycountry

country_list = list(pycountry.countries)

with open("country.js", "w") as cfile:
    cfile.write("var countries = [\n")
    for country in country_list:
        cname = country.name.encode('ascii', 'ignore').decode('ascii')
        ccode = country.alpha2.encode('ascii', 'ignore').decode('ascii')
        cfile.write("[\""+ str(ccode) + "\",\"" + str(cname) + "\"],\n")
    cfile.write("];")