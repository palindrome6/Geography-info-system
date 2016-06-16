from html import XHTML
import pycountry
import wikipedia
import gettext
import gettext
wikipedia.set_lang('fr')
french = gettext.translation('iso3166', pycountry.LOCALES_DIR,languages=['fr'])
french.install()
summary = []
lists = []
country_list = list(pycountry.countries)
for country in country_list:
    country.name = _(country.name)
    if country.name in ["Congo", "Georgia"]:
        continue
    else:
        try:
            summary1 = wikipedia.summary(country.name)
        except wikipedia.exceptions.PageError:
            lists.append(country.name)
            continue
        except wikipedia.exceptions.DisambiguationError:
            lists.append(country.name)
            continue

    print country.name
    summary1 = summary1.encode('utf-8')
    paras = summary1.split("\n")
    cname = (str(country.alpha2)).lower() + ".xhtml"
    direc = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\countries-fr\\"
    with open(direc + str(cname), "w") as cfile:
        cfile.write("<div>\n")
        for item in paras:
            cfile.write("<p>" + str(item) + "</p>\n")
        cfile.write("</div>")

with open(direc + 'exceptions.txt', "w") as tfile:
    for item in lists:
        tfile.write(item + "\n")

