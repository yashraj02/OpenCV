# THRESHOLD
import cv2 as cv

img = cv.imread('gradient.png')

_, img2 = cv.threshold(img, 117, 255, cv.THRESH_BINARY)
_, img3 = cv.threshold(img, 117, 255, cv.THRESH_BINARY_INV)
_, img4 = cv.threshold(img, 117, 255, cv.THRESH_TOZERO)
_, img5 = cv.threshold(img, 117, 255, cv.THRESH_TOZERO_INV)
_, img6 = cv.threshold(img, 117, 255, cv.THRESH_TRUNC)

cv.imshow('show2', img6)
# cv.imshow('show',img)
cv.waitKey(0)
cv.destroyAllWindows()
