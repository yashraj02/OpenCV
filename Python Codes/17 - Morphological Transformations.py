import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../Images & Videos/smarties.png', 0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

_, mask = cv.threshold(img, 200, 255, cv.THRESH_TOZERO_INV)
kernel = np.ones((5, 5), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

images = [img, mask, dilation, erosion, opening, closing, mg, th]
titles = ['Orignal', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closing', 'MG', 'TH']

for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# cv.imshow('Image1',mask)
# cv.waitKey(0)
# cv.destroyAllWindows()
