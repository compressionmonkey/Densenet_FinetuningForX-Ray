from os import listdir
from BatchReader import unpickle
import pickle
from imageTransformer import getImage
from Crawler_Annotation import TBclassification
from Crawler_Annotation import CreateFilename
location = "/Users/pc/Downloads/cifar-10-batches-py"
ClinicalReadings = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
# create a list of files in location
fileList = list(file for file in listdir(location))

class FileDir:
    def __init__(self, fileList, file, fileName):
        self.FileList = fileList
        self.file = file
        self.fileName = fileName
    def checkbatchandunpickle(self, filerequired, wantedSec):
        for file in listdir(location):
            if file.startswith(filerequired):
                fileName = location + '/' + file
                dictData = unpickle(fileName)

                wantPart = dictData[wantedSec]

        return dictData, wantPart

    def createTBList(self):
        for classIndex in range(0, 10008):
            tbIndex = TBclassification(classIndex)
            tbList.append(tbIndex)


FileLiSSSST = FileDir(fileList, None, None)
unpickledfile, Data = FileLiSSSST.checkbatchandunpickle("data_batch_1", b'labels')

tbList = []

zoom = FileLiSSSST.createTBList()
print(zoom)
for file in listdir(location):
    if file.startswith('data_batch_1'):
        fileName = location + '/' + file
        dict = unpickle(fileName)
        d1 = dict[b'labels']
        for classIndex in range(0, 10008):
            tbIndex = TBclassification(classIndex)
            tbList.append(tbIndex)

d1 = tbList
dict[b'labels'] = d1
pickle_out = open(fileName, "wb")
pickle.dump(dict, pickle_out)

pickle_out.close()

fileList = []
for file in listdir(location):
    if file.startswith('data_batch_1'):
        fileName = location + '/' + file
        dict = unpickle(fileName)
        d1 = dict[b'filenames']
        for fileIndex in range(0, 10008):
            fileXrayIndex = CreateFilename(fileIndex)
            fileXrayIndex.append(fileList)

d1 = fileList
dict[b'filenames'] = d1
pickle_out = open(fileName, "wb")
pickle.dump(dict, pickle_out)

pickle_out.close()

imageList = []
for imgIndex in range(0,10008):
    img = getImage(imgIndex)
    if img != None:

        imgConvert = img.convert("RGB")
        imgResized = imgConvert.resize((32, 32))

        imgData = list(imgResized.getdata())

        red, green, blue = zip(*imgData)
        channelArray = red + green + blue
        image =list(channelArray)
        print(imgIndex)
        imageList.append(image)

# d1 = dict[b'data']
d1 = imageList
dict[b'data'] = d1
pickle_out = open(fileName, "wb")
pickle.dump(dict, pickle_out)

pickle_out.close()
