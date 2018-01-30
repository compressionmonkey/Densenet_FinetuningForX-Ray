import os

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
for root, dirs, filenames in os.walk(Input):
 # Create a number assigned to each filename in list for auto assigned tasks later on
    for counter, value in enumerate(filenames):
            # editing a directory properly that is indexed correctly in the list that it is
        Location_File = root + '/' + filenames[counter]

        FileList.append(Location_File)

TestFile = FileList[0]

import numpy as np
from PIL import Image

i_width = 32
i_height = 32

img = Image.open(TestFile)

TestFile = img.resize((i_height, i_width))

CorrectList = []
arr = np.array(TestFile)# 32x32x4 array
 # 4-vector, just like above
for i in range(0,32):
    while i != 32:
        CorrectList = arr[i] + arr[i+1]
    else:
        i = 31
        CorrectList = arr[i] + arr[i + 1]
        print(CorrectList)
        break

im = img