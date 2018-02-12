from os import listdir
from PIL import Image
imageInput = "/Users/pc/Downloads/MontgomerySet/CXR_png"
listOfFiles = listdir(imageInput)

def getImage(indexImage):
    returnValue = None
    fileName = listOfFiles[indexImage]
    pngFormat = '.png'
    if fileName.endswith(pngFormat):
        returnValue = Image.open(imageInput + '/' + listOfFiles[indexImage])

    else:
        print(fileName)
        print('Invalid file')
    return returnValue

