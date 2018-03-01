from os import listdir
import cv2
import pandas as pd
fileDir = "/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png"

listOfFiles = listdir(fileDir)
print(listOfFiles)
class CSV():
    def __init__(self, listOfFiles):
        self.listOfFiles = listOfFiles

    # def TBclassification(indexAnnot):
    #     fileName = listOfFiles[indexAnnot]
    #     fileType = ".png"
    #     if fileName.endswith(fileType):
    #         returnValue = int(fileName[12])
    #         return returnValue
    #     else:
    #         print(fileName)
    #         print('Invalid file')
    #
    # def createTBList(self):
    #     for classIndex in range(0, 10008):
    #         tbIndex = TBclassification(classIndex)
    #         tbList.append(tbIndex)

    def FindFileBin(self):
        fileType = ".png"
        tbList = []
        for num in range(1, len(listOfFiles) - 1):
            currentFile = listOfFiles[num]
            fileName = fileDir + '/' + currentFile
            # for fileNameExact in listOfFiles:
            if currentFile.endswith(fileType):
                returnValue = int(currentFile[12])
                tbList.append(returnValue)
                if num == 662:
                    return tbList

            if fileName == "NoneType":
                break
    def FindFile(self):
        fileType = ".png"
        fileList = []
        for num in range(1, len(listOfFiles) - 1):
            currentFile = listOfFiles[num]
            fileName = fileDir + '/' + currentFile
            # for fileNameExact in listOfFiles:
            if currentFile.endswith(fileType):
                returnValue = fileName
                fileList.append(returnValue)
                if num == 662:
                    return fileList

            if fileName == "NoneType":
                break
            # return tbList
    def Twosides(self,):
        fileType = ".png"
        for img in listOfFiles:
            if img.endswith(fileType):
                for num in range(1, len(listOfFiles) - 1):

                    currentFile = listOfFiles[num]
                    fileName = fileDir + '/' + currentFile
                    img = cv2.imread(fileName, 0)

                    img2 = img.copy()
                    print(img2)
                    # Makes a copy
                    sumOfPixelsLeft = 0
                    sumOfPixelsRight = 0
                    count = 0
                    updatedImgRow = []
                    updatedImg = []
                    for pixelrow in img2:
                        for pixel in pixelrow:

                            count += 1
                            if count <= 1500:
                                sumOfPixelsLeft += pixel
                            else:
                                sumOfPixelsRight += pixel

                        updatedImgRow.append([sumOfPixelsLeft,sumOfPixelsRight])
                    # Sum = 0
                    for Sum in range(len(updatedImgRow)):
                        if Sum < len(updatedImgRow):
                            Total = updatedImgRow[Sum][0] + updatedImgRow[Sum+1][0]
                            print(Total)
                        else:
                            break
                        # sum(updatedImgRow[Sum][0])
                    # Total = updatedImgRow[sum][0] + updatedImgRow[n-1][0]
                    # updatedImgRow[n][]
                    print(updatedImgRow[0][0])
                    for x in currentFile:
                        updatedImg.append(updatedImgRow)

                    print(updatedImg)
                    # return updatedImg
                    if img == "NoneType":
                        break

csvObject = CSV(listOfFiles)
binList = csvObject.FindFileBin()
dirList = csvObject.FindFile()
pixels = csvObject.Twosides()
print(pixels)


        # fileFullName, TBbinary = CreateCSV(num)
        # print(fileFullName, TBbinary)
        # f = pd.DataFrame(data={'FileName': [fileFullName], 'TBBinary': [TBbinary], 'TotalPixelsL': [sumOfPixelsLeft], 'TotalPixelsR': [sumOfPixelsRight]})








        # f.append({'FileName': [fileFullName], 'TBBinary': [TBbinary], 'TotalPixelsL': sumOfPixelsLeft, 'TotalPixelsR': sumOfPixelsRight}, ignore_index=True)
# f.to_csv('imagedata.csv', index=False)
        # print(sumOfPixelsLeft, sumOfPixelsRight)



# csv_input = pd.read_csv('imagedata.csv')
# for fileIndex in range(len(listOfFiles)):
#     fileFullName, TBbinary = CreateCSV(fileIndex)
#     print(fileFullName, TBbinary)
#     f = pd.DataFrame(data = {'FileName':[fileFullName], 'TBBinary':[TBbinary], })
# # f.append({'FileName':[fileFullName], 'TBBinary':[TBbinary]}, ignore_index=True)
# # csv_input['Berries'] = csv_input['Name']
# f.to_csv('imagedata.csv', index=False)
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

