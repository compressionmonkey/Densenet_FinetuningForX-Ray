import os
from os import listdir
fileDir = "/Users/pc/Downloads/MontgomerySet/CXR_png"
listOfFiles = listdir(fileDir)
# check url https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256233/ for datasets
def CreateFilename(indexFiles):
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    returnValue = None
    fileName = listOfFiles[indexFiles]
    fileType = ".png"
    if fileName.endswith(fileType):
        returnValue = int(fileName)
        return returnValue
    else:
        print(fileName)
        print('Invalid file')

# Test for converting Xray into Dictionary for pickling

def TBclassification(indexAnnot):
    fileName = listOfFiles[indexAnnot]
    fileType = ".png"
    if fileName.endswith(fileType):
        returnValue = int(fileName[12])
        return returnValue
    else:
        print(fileName)
        print('Invalid file')
