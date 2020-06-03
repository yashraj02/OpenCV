import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../Images & Videos/coins.jpg')
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur
blur = cv.medianBlur(img_grey, 11)
ret, thresh = cv.threshold(blur, 70, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
morph_op = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=2)
sure_back = cv.dilate(morph_op, np.ones((3, 3), np.uint8), iterations=3)
sure_fore = cv.distanceTransform(morph_op, cv.DIST_L2, 5)
ret, sure_fore = cv.threshold(sure_fore, 20, 255, cv.THRESH_BINARY)
sure_fore = np.uint8(sure_fore)
unknown = cv.subtract(sure_back, sure_fore)
ret, markers = cv.connectedComponents(sure_fore)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv.watershed(img, markers)
Image, contours, hierarchy = cv.findContours(markers, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv.drawContours(img, contours, i, (0, 255, 0), 2)
plt.imshow(img, cmap='gray')
plt.show()
