import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png/CHNCXR_0001_0.png',0)

img2 = img.copy()
template = cv2.imread('/Users/pc/Downloads/ChinaSet_AllFiles/CXR_png/template.png',0)


sumOfPixelsLeft = 0
sumOfPixelsRight = 0
count = 0
for pixelrow in img2:
    for pixel in pixelrow:

        count += 1
        if count <= 1500:
            sumOfPixelsLeft += pixel
            print(pixel)
        else:
            sumOfPixelsRight += pixel

print(sumOfPixelsLeft, sumOfPixelsRight)
        # print(len(pixelrow))
        # print(count)

height, width = img.shape[:2]
print(img.shape)

# Let's get the starting pixel coordiantes (top left of cropped top)
start_row, start_col = int(0), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped top)
end_row, end_col = int(height * .5), int(width)
cropped_top = img[start_row:end_row , start_col:end_col]
print(start_row, end_row)
print(start_col, end_col)

cv2.imshow("Cropped Top", cropped_top)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's get the starting pixel coordiantes (top left of cropped bottom)
start_row, start_col = int(height * .5), int(0)
# Let's get the ending pixel coordinates (bottom right of cropped bottom)
end_row, end_col = int(height), int(width)
cropped_bot = img[start_row:end_row , start_col:end_col]
print(start_row, end_row)
print(start_col, end_col)

cv2.imshow("Cropped Bot", cropped_bot)
cv2.waitKey(0)
cv2.destroyAllWindows()

w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()