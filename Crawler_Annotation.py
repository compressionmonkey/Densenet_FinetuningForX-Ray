import os
from os import listdir
from PIL import Image
from BatchReader import unpickle
import pickle
# check url https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256233/ for datasets
def CreateDictionary():
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    Input = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
    FileList = []
    FileDict = {}
    for root, dirs, filenames in os.walk(Input):
        # Create a number assigned to each filename in list for auto assigned tasks later on
        for counter, value in enumerate(filenames):
            # editing a directory properly that is indexed correctly in the list that it is
            Location_File = root + '/' + filenames[counter]

            FileList.append(Location_File)

            with open(FileList[counter]) as file:
                lines = file.readlines()
                try:
                    FileDict[counter].append(lines)
                except KeyError:
                    FileDict[counter] = [lines]
                    print(FileDict)


# Test for converting Xray into Dictionary for pickling

Input = "/Users/pc/Downloads/MontgomerySet/CXR_png"
FileList = []
FileDict = {}
fileType = ".png"
for root, dirs, filenames in os.walk(Input):
 # Create a number assigned to each filename in list for auto assigned tasks later on
    for counter, value in enumerate(filenames):
            # editing a directory properly that is indexed correctly in the list that it is
        if filenames[counter].endswith(fileType):
            Location_File = int(filenames[counter][12])

            FileList.append(Location_File)
print(len(FileList))