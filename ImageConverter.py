from PIL import Image
import numpy as np
from random import randint


# create random array
def create_arr(width, height):
    bin_array = np.zeros((width, height), 'uint8')
    for x in range(0, width):
        for y in range(0, height):
            bin_array[x, y] = randint(0, 1)
    return bin_array

# write array to img
def create_img(width, height, bin_array):
    rgb_array = np.zeros((width, height, 3), 'uint8')
    for x in range(0, width):
        for y in range(0, height):
            rgb_array[x, y, 0] = bin_array[x, y] * 255 #R
            rgb_array[x, y, 1] = bin_array[x, y] * 255 #G
            rgb_array[x, y, 2] = bin_array[x, y] * 255 #B

    img = Image.fromarray(rgb_array)
    img.save('img.jpeg')

# create array
bin_array = create_arr(64, 64)
# write bin_array to img
create_img(64, 64, bin_array)