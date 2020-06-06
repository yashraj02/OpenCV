import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/russian_license_plate.jfif')
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
license_cascade = cv.CascadeClassifier('../Images & Videos/russin_license_plate2.xml')
license_plate = license_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=2)
black_img = np.zeros((img.shape), dtype=np.uint8)
for (x, y, w, h) in license_plate:
    blur = cv.medianBlur(img[y:y + h, x:x + w], 15)
    img[y:y + h, x:x + w] = blur
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
