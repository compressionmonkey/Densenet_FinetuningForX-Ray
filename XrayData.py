from os import listdir
from BatchReader import unpickle
import pickle
from imageTransformer import getImage
from Crawler_Annotation import TBclassification

location = "/Users/pc/Downloads/cifar-10-batches-py"
ClinicalReadings = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
# create a list of files in location
FileList = list(file for file in listdir(location))

# Uses FileList to unpickle and create dictionaries out of files not readable

# Create a transformer to convert all batch images into black
tbList = []
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

tbList = []
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
