import xmltodict
import json

#im too lazy to make another practice file
#So i will simply take the json file I made and turn that into XML

#json -> python dictionary -> xml

#opening the json file and turning it into a dictionary
with open("devices.json") as f:
    openFile = f.read()
    jsonDict = json.loads(openFile)

#our json has multiple roots, but xml can only have one root
#we will simply create another dictionary, with our original dictionary as the value
newDict = {"network": jsonDict}

#turning the python dict into xml
xmlString = xmltodict.unparse(newDict, pretty= True) #pretty=True, so we dont get 1 long line

#saving the xmlString as a file
with open("devices.xml", "w") as f:
    f.write(xmlString)
    