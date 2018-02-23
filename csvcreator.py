from os import listdir
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
for fileIndex in range(1,len(listOfFiles)):
    print(fileIndex)
    fileFullName, TBbinary = CreateCSV(fileIndex)
    print(fileFullName, TBbinary)
    fileList.append(fileFullName)

print(fileList)


