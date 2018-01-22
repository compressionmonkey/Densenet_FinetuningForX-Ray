from __future__ import absolute_import
from keras.datasets.cifar import load_batch
from keras.utils.data_utils import get_file
from keras import backend as K
import numpy as np
import os
from os import listdir
from BatchReader import unpickle

location = "/Users/pc/Downloads/cifar-10-batches-py"
ClinicalReadings = "/Users/pc/Downloads/MontgomerySet/ClinicalReadings"
# create a list of files in location
FileList = list(file for file in listdir(location))

# Uses FileList to unpickle and create dictionaries out of files not readable

def transform_data(location):
    for file in listdir(location):
        if file.startswith('data_batch_1'):
            dict = unpickle(location + '/' + file)
            print(dict)

transform_data(location)


def SwapImages(Input=location, exchange=ClinicalReadings):
    for file in listdir(location):
        dict = unpickle(location + '/' + file)
        for iterations in dict:
            print(iterations)

SwapImages(location, ClinicalReadings)

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
