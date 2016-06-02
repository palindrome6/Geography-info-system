from html import XHTML
import pycountry
import wikipedia

summary = []
continent_names = ["Australia and New Zealand", "Melanesia", "Micronesia", "Polynesia", "Earth"]
for continent in continent_names:
    summary1 = wikipedia.summary(continent)
    print continent
    summary1 = summary1.encode('utf-8')
    paras = summary1.split("\n")
    cname = continent.lower() + ".xhtml"
    direc = "C:\Users\s158079\Downloads\Study_materials\Quartile 4\Adaptive web\Project\continents\\"
    with open(direc + str(cname), "w") as cfile:
        cfile.write("<div>\n")
        for item in paras:
            cfile.write("<p>" + str(item) + "</p>\n")
        cfile.write("</div>")

