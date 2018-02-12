import os
from os import listdir
fileDir = "/Users/pc/Downloads/MontgomerySet/CXR_png"
listOfFiles = listdir(fileDir)
# check url https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256233/ for datasets
def CreateDictionary(indexFiles):
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    returnValue = None
    fileName = listOfFiles[indexFiles]
    fileType = ".png"
    if fileName.endswith(fileType):
        returnValue = int(fileName)
    else:
        print(fileName)
        print('Invalid file')

    return returnValue

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


def TBclassification(indexAnnot):
    returnValue = None
    fileName = listOfFiles[indexAnnot]
    fileType = ".png"
    if fileName.endswith(fileType):
        returnValue = int(fileName[12])
    else:
        print(fileName)
        print('Invalid file')
        TBclassification(indexAnnot+1)

    return returnValue