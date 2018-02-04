from os import listdir
from PIL import Image
imageInput = "/Users/pc/Downloads/MontgomerySet/CXR_png"
listOfFiles = listdir(imageInput)

def getImage(indexImage):
    return Image.open(listOfFiles[indexImage])