import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)

_, img2 = cv.threshold(img, 117, 255, cv.THRESH_BINARY)
_, img3 = cv.threshold(img, 117, 255, cv.THRESH_BINARY_INV)
_, img4 = cv.threshold(img, 117, 255, cv.THRESH_TOZERO)
_, img5 = cv.threshold(img, 117, 255, cv.THRESH_TOZERO_INV)
_, img6 = cv.threshold(img, 117, 255, cv.THRESH_TRUNC)

images = [img, img2, img3, img4, img5, img6]
titles = ['Orignal', 'Binary', 'Inverse', 'Tozero', 'Tozero_Inv', 'Trunc']

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv.imshow('show2',img6)
# cv.imshow('show',img)
# cv.waitKey(0)
cv.destroyAllWindows()
