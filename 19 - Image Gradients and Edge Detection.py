# Image Gradient - directional change in color of an image
# Methods() for detecting edges - Laplacian Derivaties (edges)| Sobel X (verti. edges) | Sobel Y (horiz. edges)
# -----------------------------------------------------

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', 0)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian = np.uint8(np.absolute((laplacian)))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute((sobelX)))
sobelY = np.uint8(np.absolute((sobelY)))

sobel_combined = cv.bitwise_or(sobelX, sobelY)

images = [img, laplacian, sobelX, sobelY, sobel_combined]
titles = ['Orignal', 'Laplacian', 'SobelX', 'SobelY', 'Sobel_Combined']

for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
# cv.imshow('show',img)
cv.waitKey(0)
cv.destroyAllWindows()
