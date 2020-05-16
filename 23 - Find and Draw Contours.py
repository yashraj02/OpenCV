# Contours are the curves joining all the continuous points along the boundary which have same color or intensity
# Used for shape analysis object detection or object recognitions
# Binary image to find contours

# First find threshold then pass it to findContours to derieve countours

import cv2 as cv

img = cv.imread('opencv-logo.png')
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# finding threshold
ret, threshold = cv.threshold(img2, 127, 255, 0)
contours, hierarchy = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('Number of Contours: ', len(contours))
cv.drawContours(img, contours, -1, (0, 255, 0), 4)

cv.imshow('1', img)
cv.waitKey(0)
cv.destroyAllWindows()
