import json
#this code reads json and parses it
#.load() = imports native json and turns it into a python dict
#.loads() = import json data from a string 
#.dump() = used to write json data from python objects to a file
#.dumps() = takes json formatted strings and turns it into an appropiate type in python 



#reading json file and turning it into a python dictionary
def readJson(): 
    with open("devices.json") as f:
        jsonString = f.read() 
        jsonDict = json.loads(jsonString)
        return jsonDict

#function for printing out only switches, able to show switches by location (optional)      
def getSwitch(dataDict, location = ""):
    missingLocation = True
    for switch in dataDict["networkDevices"]["switches"]:
        if location.lower() == (switch["location"].lower()) or (location == ""):
            missingLocation = False
            print(f"Hostname: {switch['hostname']}")
            print(f"Ip-Address: {switch['ip-address']}")
            print(f"Location: {switch['location']}", end = "\n\n")
    if missingLocation == True:
        print(f"No switches found in location: {location}")
  



def main():  #this is where the user can change the script to get their desired results
    myData = readJson()
    getSwitch(myData, "")


if __name__ == "__main__":
    main()


 