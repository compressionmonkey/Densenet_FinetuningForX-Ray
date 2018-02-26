from os import listdir
import cv2
import pandas as pd
fileDir = "/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png"

listOfFiles = listdir(fileDir)

# fileName = listOfFiles[1]
# fileType = ".png"
# for fileNameExact in listOfFiles:
#     if fileNameExact.endswith(fileType):
#         returnValue = int(fileNameExact[12])
#         print(fileNameExact, returnValue)
def CreateCSV(indexFiles):
    # We want to create a dictionary to number and list out all of our values i.e patient annotation details
    fileIndex = 0
    # fileName = listOfFiles[indexFiles]
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

# fileList = []
# TBList = []
# for fileIndex in range(1,len(listOfFiles)):
#     print(fileIndex)
#     fileFullName, TBbinary = CreateCSV(fileIndex)
#     print(fileFullName, TBbinary)
#     fileList.append(fileFullName)
#     TBList.append(TBbinary)
#
# print(TBList)

# f = pd.DataFrame(data = {'FileName':"-", 'TBBinary':"-", 'TotalPixelsL': "-", 'TotalPixelsR': "-"})

fileType = ".png"
for img in listOfFiles:
    if img.endswith(fileType):
        returnValue = int(img[12])
        fileFullName, TBbinary = img, returnValue
        print(fileFullName, TBbinary)
        for num in range(1, len(listOfFiles)):

            currentFile = listOfFiles[num]
            fileName = fileDir + '/' + currentFile
            img = cv2.imread(fileName, 0)

            img2 = img.copy()

            sumOfPixelsLeft = 0
            sumOfPixelsRight = 0
            count = 0
            for pixelrow in img2:
                for pixel in pixelrow:

                    count += 1
                    if count <= 1500:
                        sumOfPixelsLeft += pixel
                    else:
                        sumOfPixelsRight += pixel

        # fileFullName, TBbinary = CreateCSV(num)
        print(fileFullName, TBbinary)
        f = pd.DataFrame(data={'FileName': [fileFullName], 'TBBinary': [TBbinary], 'TotalPixelsL': [sumOfPixelsLeft], 'TotalPixelsR': [sumOfPixelsRight]})

    if img == "NoneType":
        break






        # f.append({'FileName': [fileFullName], 'TBBinary': [TBbinary], 'TotalPixelsL': sumOfPixelsLeft, 'TotalPixelsR': sumOfPixelsRight}, ignore_index=True)
f.to_csv('imagedata.csv', index=False)
        # print(sumOfPixelsLeft, sumOfPixelsRight)



# csv_input = pd.read_csv('imagedata.csv')
# for fileIndex in range(len(listOfFiles)):
#     fileFullName, TBbinary = CreateCSV(fileIndex)
#     print(fileFullName, TBbinary)
#     f = pd.DataFrame(data = {'FileName':[fileFullName], 'TBBinary':[TBbinary], })
# # f.append({'FileName':[fileFullName], 'TBBinary':[TBbinary]}, ignore_index=True)
# # csv_input['Berries'] = csv_input['Name']
# f.to_csv('imagedata.csv', index=False)
import csv
# changes = fileList, TBList

# new_rows = []
# with open('imagedata.csv', 'r') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         print(row)
#         new_row = row
#         for key, value in changes.items():  # iterate over 'changes' dictionary
#             new_row = [sub.replace(key, value) for sub in new_row]  # make the substitutions
#             print(new_row)
#         new_rows.append(new_row)

# fileList = []
# TBList = []
# for fileIndex in range(1,len(listOfFiles)):
#     print(fileIndex)
#     fileFullName, TBbinary = CreateCSV(fileIndex)
#     print(fileFullName, TBbinary)
#     fileList.append(fileFullName)
#     TBList.append(TBbinary)




# >>> print row0
# ['Name', 'Code', 'berry']
# >>> for item in r:
# ...     item.append(item[0])
# ...     print item
# ...
# ['blackberry', '1', 'blackberry']
# ['wineberry', '2', 'wineberry']
# ['rasberry', '1', 'rasberry']
# ['blueberry', '1', 'blueberry']
# ['mulberry', '2', 'mulberry']

# with open('imagedata.csv', 'a') as File:
#     r = csv.reader(File)
#     row0 = r.next()
#     row0.append('berry')
#     # writer = csv.writer(File)
#     for fileIndex in range(1, len(listOfFiles)):
#         fileFullName, TBbinary = CreateCSV(fileIndex)
#         print(fileFullName, TBbinary)
        # writer.writerows([[fileFullName], [TBbinary]])




# >>> f
#   Animal Color
# 0    cow  blue
# 1  horse   red

