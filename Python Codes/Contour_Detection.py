import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../Images & Videos/smilies.jpg', 0)
img = cv.resize(img, (300, 300))
img = cv.bitwise_not(img)
template = np.zeros(img.shape)
# finding threshold
ret, img = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv.drawContours(template, contours, i, (255, 255, 255), -1)
plt.imshow(img, cmap='gray')
plt.show()
# cv.imshow('show',template)
# cv.waitKey(0)
# cv.destroyAllWindows()
