import json
#I want to make one function for getting any sort of device
#And only one function for adding a device.

def readJson():
    with open("devices.json") as f:
        jsonString = f.read() 
        jsonDict = json.loads(jsonString)
        return jsonDict

def getDevice(deviceGroup, deviceType, deviceList, deviceLocation = ""):
    noLocation = True
    for device in deviceList[deviceGroup][deviceType]:
        if (deviceLocation == device["location"]) or (deviceLocation == ""):
            noLocation = False
            print(f"Hostname: {device['hostname']}")
            print(f"Ip-Address: {device['ip-address']}")
            print(f"Location: {device['location']}", end = "\n\n")
    if noLocation == True:
        print(f"No devices in location {deviceLocation}")
    

def addDevice(deviceGroup, deviceType, deviceList, deviceData):
    deviceList[deviceGroup][deviceType].append(deviceData)
    newDeviceList = json.dumps(deviceList, indent = 4)
    print(newDeviceList)



def main():           #where the user can change the script
    myData = readJson()
    #getDevice("networkDevices", "routers", myData)
    newDevice = {
        "hostname" : "jonathan's pc",
        "ip address": "192.168.3.1",
        "addressing-method": "static",
        "location": "Wellington"
    }
    addDevice("clientDevices", "computers", myData, newDevice )




if __name__ == "__main__":
    main()