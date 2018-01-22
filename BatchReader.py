def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

# def SwapImages():
#     for

# dict = unpickle('/Users/pc/Downloads/cifar-10-batches-py/data_batch_1')
# print(dict)
# import cv2 as cv
# from PIL import Image
# im = Image.open("/Users/pc/Downloads/MontgomerySet/CXR_png/MCUCXR_0001_0.png")
# # red, green, blue = cv.split()
# # print(red)
# width, height = im.size
# print(width, height)
#
# # I downsize the image with an ANTIALIAS filter (gives the highest quality)
# foo = im.resize((32,32),Image.ANTIALIAS)
# # foo.save("/Users/pc/Downloads/MontgomerySet/K/1.jpg",quality=95)
#  # The saved downsized image size is 24.8kb
# foo.save("/Users/pc/Downloads/MontgomerySet/K/3.jpg",optimize=True,quality=95)
#
# cvimage = cv.imread("/Users/pc/Downloads/MontgomerySet/K/3.jpg")
# red, green, blue = cv.split(cvimage)
# print(red)                       # The saved downsized image size is 22.9kb
