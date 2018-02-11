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

        # if indexImage >= 137:
        #     numberToGo = 10000 - indexImage
        #     returnValue = Image.open(imageInput + '/' + listOfFiles[1])
        #     indexImage = 0
        #     # imgIndex = 0
        #     numberToGo += 1
        #     print("Over 137")

    else:
        print(fileName)
        print('Invalid file')
    return returnValue

