import pycountry

f = open('countrylist.txt','r')
country = f.read() 
countrylist = country.splitlines()
countrylist2 = []

for i in countrylist:
	countrylist2.append(i.split(','))
print(countrylist2)

output = open('concept.gam','w')

#generate body
header = "$options { default.properties \"event;strict\"}"
index = "index {" + '\n' + '\t' + '#resource = `~ return "[[=index.xhtml]]";`' + '\n' + '}'

output.write(header + '\n' + index + '\n')

for i in countrylist2:
	ConceptName = i[0]
	ContentFile = i[0].lower().replace(' ','_') + '.xhtml'
	level = int(i[1])

	if level == 0:
		ParentName = ""
		ZeroParentLevel = ConceptName.replace(' ','-').lower()
		line = ConceptName.replace(' ','-').lower() + ' {' + '\n' + '\t'
		line2 = 'title `' + ConceptName + '`' + '\n' + '\t'
		line3 = "#content:String =`~ return \"[[=content/" + ContentFile + "]]\";`" + '\n' + '\t'
		line4 = "#resource = `~ return \"[[=layout.xhtml]]\";`" + '\n' + '}' + '\n'
		output.write(line + line2 + line3 + line4)

	elif level == 1:
		ParentName = ZeroParentLevel
		FirstParentLevel = ConceptName.replace(' ','-').lower()
		line = ConceptName.replace(' ','-').lower() + ' {' + '\n' + '\t'
		line1 = "->(parent)" + ParentName.lower() + '\n' + '\t'
		line2 = 'title `' + ConceptName + '`' + '\n' + '\t'
		line3 = "#content:String =`~ return \"[[=content/" + ContentFile + "]]\";`" + '\n' + '\t'
		line4 = "#resource = `~ return \"[[=layout.xhtml]]\";`" + '\n' + '}' + '\n'
		output.write(line + line1 + line2 + line3 + line4)

	elif level == 2:
		ParentName = FirstParentLevel
		SecondParentLevel = ConceptName.replace(' ','-').lower()
		line = ConceptName.replace(' ','-').lower() + ' {' + '\n' + '\t'
		line1 = "->(parent)" + ParentName.lower() + '\n' + '\t'
		line2 = 'title `' + ConceptName + '`' + '\n' + '\t'
		line3 = "#content:String =`~ return \"[[=content/" + ContentFile + "]]\";`" + '\n' + '\t'
		line4 = "#resource = `~ return \"[[=layout.xhtml]]\";`" + '\n' + '}' + '\n'
		output.write(line + line1 + line2 + line3 + line4)

	elif level == 3:
		ParentName = SecondParentLevel
		ThirdParentLevel = ConceptName.replace(' ','-').lower()
		countryname = pycountry.countries.get(alpha2=ConceptName).name.encode('ascii', 'ignore').decode('ascii')
		#print countryname
		line = ConceptName.replace(' ','-').lower() + ' {' + '\n' + '\t'
		line1 = "->(parent)" + ParentName.lower() + '\n' + '\t'
		line2 = 'title `' + countryname + '`' + '\n' + '\t'
		line3 = "#content:String =`~ return \"[[=content/" + ContentFile + "]]\";`" + '\n' + '\t'
		line4 = "#resource = `~ return \"[[=layout.xhtml]]\";`" + '\n' + '}' + '\n'
		output.write(line + line1 + line2 + line3 + line4)
	output.write('\n')

output.close()

f.close()