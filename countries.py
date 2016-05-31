from html import XHTML
import pycountry
import wikipedia

# print wikipedia.summary("India")

country_list = list(pycountry.countries)
i = 1
for country in country_list:
    print country.name
    summary1 = wikipedia.summary(str(country.name))
    summary1 = summary1.encode('utf-8')
    h = XHTML()
    h.div(summary1)
    cname = str(country.name) + ".xhtml"
    with open(str(cname), "w") as cfile:
        cfile.write(str(h))
    print i
    i += 1
    break