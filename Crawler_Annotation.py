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
for root, dirs, filenames in os.walk(Input):
 # Create a number assigned to each filename in list for auto assigned tasks later on
    for counter, value in enumerate(filenames):
            # editing a directory properly that is indexed correctly in the list that it is
        Location_File = root + '/' + filenames[counter]

        FileList.append(Location_File)

TestFile = FileList

imageInput = "/Users/pc/Downloads/MontgomerySet/CXR_png"
FileList = []
FileDict = {}
for file in listdir(imageInput):
        fileName = imageInput + '/' + file
        FileList.append(fileName)
        if fileName != "/Users/pc/Downloads/MontgomerySet/CXR_png/Thumbs.db":
            for imgIndex in range(0,10000):
                # Index our images
                img = Image.open(fileName)
                print(img)
                # image = d1[imgIndex]
                # print(image)

            # pixels = list(img.getdata())
            # print(pixels)
                imgResized = img.resize((32, 32))
                imgData = imgResized.getdata()
                pixels = list(imgData)
                red, green, blue = zip(*pixels)
                channelArray = red + green + blue
                image = list(channelArray)
                print(image)
            # for chanelValueIndex in range(0, 3072):
            # chanelValue = image[chanelValueIndex]
        else:
            break



import numpy as np
from PIL import Image
from scipy import misc
# img = misc.imread(TestFile)

i_width = 32
i_height = 32
n = range(0,10000)
print(n)
img = Image.open(TestFile)

TestFile = img.resize((i_height, i_width))
# arr = img.load(TestFile)
CorrectList = []
pixels = list(TestFile.getdata())
print(pixels)
arr = np.array(TestFile)# 32x32x4 array
 # 4-vector, just like above
for i in range(0,32):
    CorrectList.extend(arr[i])

    # while i != 32:
    #     CorrectList = arr[i] + arr[i+1]
    # else:
    #     i = 31
    #     CorrectList = arr[i] + arr[i + 1]
    #     print(CorrectList)
    #     break
print(CorrectList)

for n in range(0,10000):
    img = Image.open(TestFile[n])
pixels = list(img.getdata())

imgResized = img.resize((i_height, i_width))

imgData = imgResized.getdata()
pixels = list(imgData)

red,green,blue = zip(*pixels )
channelArray = red+green+blue
print(channelArray)
