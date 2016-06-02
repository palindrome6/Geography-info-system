from html import XHTML
import pycountry
import wikipedia

summary = []
country_list = list(pycountry.countries)
for country in country_list:
    if country.name in ["Congo", "Georgia"]:
        continue
    else:
        summary1 = wikipedia.summary(country.name)
    print country.name
    summary1 = summary1.encode('utf-8')
    paras = summary1.split("\n")
    cname = (str(country.alpha2)).lower() + ".xhtml"
    direc = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\countries\\"
    with open(direc + str(cname), "w") as cfile:
        cfile.write("<div>\n")
        for item in paras:
            cfile.write("<p>" + str(item) + "</p>\n")
        cfile.write("</div>")

