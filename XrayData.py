from os import listdir
from BatchReader import unpickle
import pickle
from imageTransformer import getImage
from Crawler_Annotation import TBclassification
from Crawler_Annotation import CreateFilename
location = "/Users/pc/Downloads/cifar-10-batches-py-copy1"
ClinicalReadings = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
# create a list of files in location
fileList = list(file for file in listdir(location))

class FileDir:
    def __init__(self, fileList):
        self.fileList = fileList
    def checkbatchandunpickle(self, filerequired, wantedSec):
        for file in listdir(location):
            if file.startswith(filerequired):
                fileName = location + '/' + file
                dictData = unpickle(fileName)
                # transferData = dictData[wantedSec]
                # dictData[wantedSec] = transferData
                # wantPart = transferData
                wantPart = dictData[wantedSec]

        return dictData, wantPart

    def createTBList(self):
        for classIndex in range(0, 10008):
            tbIndex = TBclassification(classIndex)
            tbList.append(tbIndex)

    def swapList(self, fileName, partrequired, usedList):
        unpickledfile[partrequired] = usedList
        print(unpickledfile[partrequired])
        pickle_out = open(fileName, "wb")
        pickle.dump(dict, pickle_out)
        pickle_out.close()

    def createXrayList(self):
        # d1 = dict[b'filenames']
        for fileIndex in range(0, 10008):
            fileXrayIndex = CreateFilename(fileIndex)
            print(fileXrayIndex)
            fileXrayIndex.append(fileList)

    def collectPixels(self):
        for imgIndex in range(0, 10008):
            img = getImage(imgIndex)
            if img != None:
                imgConvert = img.convert("RGB")
                imgResized = imgConvert.resize((32, 32))

                imgData = list(imgResized.getdata())

                red, green, blue = zip(*imgData)
                channelArray = red + green + blue
                image = list(channelArray)
                print(imgIndex)
                imageList.append(image)

FileLiSSSST = FileDir(fileList)
unpickledfile, Data = FileLiSSSST.checkbatchandunpickle("data_batch_1", b'labels')

tbList = []

FileLiSSSST.createTBList()
print(tbList)

FileLiSSSST.swapList(location + "/data_batch_1", b'labels', tbList)

fileList = []
FileLiSSSST.createXrayList()
print(fileList)

FileLiSSSST.swapList(location + "/data_batch_1", b'filenames', fileList)


imageList = []
FileLiSSSST.collectPixels()
print(imageList)
FileLiSSSST.swapList(location + "/data_batch_1", b'data', imageList)
