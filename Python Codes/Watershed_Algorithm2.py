import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../Images & Videos/coins.jpg')
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(img_grey, ksize=11)
ret, thresh = cv.threshold(blur, 70, 255, cv.THRESH_BINARY)
sure_back = cv.dilate(thresh, (5, 5), iterations=2)
sure_fore = cv.distanceTransform(thresh, cv.DIST_L2, 5)
ret, sure_fore = cv.threshold(sure_fore, 20, 255, cv.THRESH_BINARY)
sure_fore = np.uint8(sure_fore)
ret, matchers = cv.connectedComponents(sure_fore)
print(matchers.min(), matchers.max())
unknown = cv.subtract(sure_back, sure_fore)
matchers[matchers == 1] = 2
matchers[matchers == 0] = 1
matchers[unknown == 255] = 0
ws = cv.watershed(img, markers=matchers)
image, contours, hierarchy = cv.findContours(ws, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv.drawContours(img, contours, i, (0, 255, 0), 2)
plt.imshow(img, cmap='gray')
plt.show()
