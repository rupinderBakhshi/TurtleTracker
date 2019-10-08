#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Parses a line of ARGOS tracking data 
#
# Created by: Rupinder Bakhshi (rupinder.bakhshi@duke.edu)
# Created on: Fall 2019
#--------------------------------------------------------------

# Create a variable pointing to the file with no header
fileName ="Data/Raw/sara.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Read the first line from the open file object
lineStrings = fileObj.readlines()
print ("There are {} records in the file".format(len(lineStrings)))
    
# Close the file object
fileObj.close()

# Create empty dictionaries
dateDict = {}
locationDict = {}

# Use a for loop to read each line, one at a time, until the list is exhausted
for lineString in lineStrings:
    #Skip the non-data lines
    if lineString[0] !='2': continue

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")
    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

# Filters out records
    if obsLC in ('1','2','3'):
        # Add values to dictionary
        dateDict[recordID] = obsDate   
        locationDict[recordID] = (obsLat, obsLon) 

#Ask user for date
userDate= input("Enter a date M/D/YYYY:")

# collect keys matching user date
keyList=[]
for k,v in dateDict.items():
     if v== userDate:
         keyList.append(k)
  # Report if no keys are found
if len(keyList)==0:
    print("No records found for {}".format(userDate)) 
else:
    #show coordinates
    for key in keyList:
        theCoordinate= locationDict[key]
        print("Turtle found at {}".format(theCoordinate))
