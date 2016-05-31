from html import XHTML
import pycountry
import wikipedia

summary = []
country_list = list(pycountry.countries)
for country in country_list:
    print country.name
    summary1 = wikipedia.summary(country.name)
    summary1 = summary1.encode('utf-8')
    h = XHTML()
    h.div(summary1)
    cname = (str(country.alpha2)).lower() + ".xhtml"
    with open(str(cname), "w") as cfile:
        cfile.write(str(h))
    summary1 = str(summary1)
