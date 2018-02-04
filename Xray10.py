from __future__ import absolute_import
from keras.datasets.cifar import load_batch
from keras.utils.data_utils import get_file
from keras import backend as K
import numpy as np
import os
from os import listdir
from BatchReader import unpickle
# from Crawler_Annotation import CreateDictionary
from PIL import Image
from pandas.core.frame import DataFrame
import skimage
import pickle
location = "/Users/pc/Downloads/cifar-10-batches-py"
ClinicalReadings = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
# create a list of files in location
FileList = list(file for file in listdir(location))

# Uses FileList to unpickle and create dictionaries out of files not readable
# for file in listdir(location):
#     if file.startswith('data_batch_1'):
#         Dict = unpickle(location + '/' + file)
#         D1 = Dict[b'data'][3]
#
#         data = [3072]
#         NewImage = Image.new('RGB', (32, 32))
#
#         PixelList = []
#
#         for i in range(0, 1024):
#             pixel = (D1[i], D1[i + 1024], D1[i + 2048])
#             PixelList.append(pixel)
#             # print(PixelList)
#
#         NewImage.putdata(PixelList)
#
#         NewImage.save('test.jpg')


# Create a transformer to convert all batch images into black

for file in listdir(location):
    if file.startswith('data_batch_1'):
        fileName = location + '/' + file
        dict = unpickle(fileName)
        d1 = dict[b'data']
        pixelList = []
        for imgIndex in range(0,10000):
            # Index our images
            image = d1[imgIndex]
            print(image)
            img = Image.open('test.jpg')
            pixels = list(img.getdata())

            imgResized = img.resize((32, 32))

            imgData = imgResized.getdata()
            pixels = list(imgData)

            red, green, blue = zip(*pixels)
            channelArray = red + green + blue
            image =list(channelArray)
            # for chanelValueIndex in range(0, 3072):
            #     chanelValue = image[chanelValueIndex]
            #     #print(chanelValue)
            #     #if(chanelValue==0):
            #     #    print("File transformed already")
            #     image[chanelValueIndex] = 0
            print(imgIndex)
            print(image)
        #ununpickle
        pickle_out = open(fileName, "wb")
        pickle.dump(dict, pickle_out)
        pickle_out.close()
            # for image in d1[index]:
            #     for numIndex, value in enumerate(d1[index]):
            #         if value.strip() != d1[index][numIndex]:
            #             d1[index][numIndex] = 0
            #             print(d1[index])
                    # if number != 2:
                    #     Dekpa = 0
                    #     print(D1[images])
                    # else:
                    #     break
                        # D1[n].append(Dekpa)
                    # print(D1[n])
                # print(PixelValues)
            # print(PixelList)

def transform_data(location):
    for file in listdir(location):
        if file.startswith('data_batch_1'):
            Dict = unpickle(location + '/' + file)
            # print(Dict[b'data'][0])
            # print(len(Dict[b'data']))
transform_data(location)


# def SwapDictionary(Input=location, exchange=ClinicalReadings):
#     for file in listdir(location):
#         if file.startswith('data_batch_1'):
#             Dict = unpickle(location + '/' + file)
#             mydict = dict((k, v) for k, v in Dict.items())
#
# SwapDictionary(location, ClinicalReadings)

def load_data():
    """Loads CIFAR10 dataset.

    # Returns
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """
    Image = np.load('/Users/pc/Downloads/MontgomerySet/CXR_png')
    ClinicalReading = np.load('/Users/pc/Downloads/MontgomerySet/ClinicalReadings')
    dirname = 'cifar-10-batches-py'
    origin = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    path = get_file(dirname, origin=origin, untar=True)

    # create function to transform the data
    # create fucntiom to take in the path

    num_train_samples = 50000

    x_train = np.empty((num_train_samples, 3, 32, 32), dtype='uint8')
    y_train = np.empty((num_train_samples,), dtype='uint8')

    for i in range(1, 6):
        fpath = os.path.join(path, 'data_batch_' + str(i))
        (x_train[(i - 1) * 10000: i * 10000, :, :, :],
         y_train[(i - 1) * 10000: i * 10000]) = load_batch(fpath)

    fpath = os.path.join(path, 'test_batch')
    x_test, y_test = load_batch(fpath)

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    if K.image_data_format() == 'channels_last':
        x_train = x_train.transpose(0, 2, 3, 1)
        x_test = x_test.transpose(0, 2, 3, 1)

    return (x_train, y_train), (x_test, y_test)
