from html import XHTML
import pycountry
import wikipedia

continent_names = ["Africa", "Americas", "Asia", "Europe", "Oceania"]

for continent in continent_names:
    summary1 = wikipedia.summary(continent)
    print continent
    summary1 = summary1.encode('utf-8')
    h = XHTML()
    h.div(summary1)
    cname = (str(continent)).lower() + ".xhtml"
    direc = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\continents\\"
    with open(direc + str(cname), "w") as cfile:
        cfile.write(str(h))
    summary1 = str(summary1)
