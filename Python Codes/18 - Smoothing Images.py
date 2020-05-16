# Smoothing/Blurring - softens corners by blur
# Linear Filter - To remove noise
# filter2D
# Low pass filter - removing noise by blur
# High pass filters - finding edges in images


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('Half')
img = cv.imread('../Images & Videos/water.jfif')
# img = cv.imread('lena.jpg')
# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
# Median Filter - salt & pepper noise (kernel size odd except 1)
median = cv.medianBlur(img, 5)
# when we want smooth image but sharp edges
bilateral_filter = cv.bilateralFilter(img, 9, 75, 75)

images = [img, dst, blur, gblur, median, bilateral_filter]
titles = ['Orignal', '2D Convolution', 'Blur', 'Gblur', 'Median', 'bilateral_filter']

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
