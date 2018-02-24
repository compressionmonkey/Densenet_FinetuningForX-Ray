from os import listdir
import cv2
fileDir = "/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png"

listOfFiles = listdir(fileDir)

def CreateCSV(indexFiles):
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    fileIndex = 0
    fileName = listOfFiles[indexFiles]
    fileType = ".png"
    for fileNameExact in listOfFiles:
        if fileNameExact.endswith(fileType):
            returnValue = int(fileNameExact[12])
            return fileNameExact, returnValue
        if fileName == "NoneType":
        # fileIndex += 1
            break
        # print(fileName)
        # print('Invalid file')

fileList = []
TBList = []
for fileIndex in range(1,len(listOfFiles)):
    print(fileIndex)
    fileFullName, TBbinary = CreateCSV(fileIndex)
    print(fileFullName, TBbinary)
    fileList.append(fileFullName)
    TBList.append(TBbinary)

print(fileList)

img = cv2.imread('/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png/CHNCXR_0001_0.png',0)

img2 = img.copy()

sumOfPixelsLeft = 0
sumOfPixelsRight = 0
count = 0
for pixelrow in img2:
    for pixel in pixelrow:

        count += 1
        if count <= 1500:
            sumOfPixelsLeft += pixel
            print(pixel)
        else:
            sumOfPixelsRight += pixel


print(sumOfPixelsLeft, sumOfPixelsRight)


import csv
changes = ['Dorji', 'Kelden']

new_rows = []
# with open('imagedata.csv', 'r') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         print(row)
#         new_row = row
#         for key, value in changes.items():  # iterate over 'changes' dictionary
#             new_row = [sub.replace(key, value) for sub in new_row]  # make the substitutions
#             print(new_row)
#         new_rows.append(new_row)

with open('imagedata.csv', 'a') as File:

    writer = csv.writer(File)
    writer.writerows([changes])

