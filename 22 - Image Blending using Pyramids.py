# Load 2 images
# Find Gaussian Pyramids of 6 levels
# Find Laplacian Pyraminds from Gaussian
# Join Left apple & Right Orange Laplasian
# now reconstruct joined image

import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

divided_image = np.hstack((apple[:, :256], orange[:, 256:]))

gaussian_apple = apple.copy()
gaussian_apple_list = [gaussian_apple]
for i in range(6):
    gaussian_apple = cv.pyrDown(gaussian_apple);
    gaussian_apple_list.append(gaussian_apple)
    # cv.imshow(str(i),gaussian_apple)

gaussian_orange = orange.copy()
gaussian_orange_list = [gaussian_orange]
for i in range(6):
    print(i)
    gaussian_orange = cv.pyrDown(gaussian_orange);
    gaussian_orange_list.append(gaussian_orange)
    # cv.imshow(str(i),gaussian_orange)

laplasian_apple_list = [gaussian_apple_list[6]]
for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gaussian_apple_list[i])
    laplasian = cv.subtract(gaussian_apple_list[i - 1], gaussian_extended)
    laplasian_apple_list.append(laplasian)

laplasian_orange_list = [gaussian_orange_list[6]]
for i in range(6, 0, -1):
    gaussian_extended = cv.pyrUp(gaussian_orange_list[i])
    laplasian = cv.subtract(gaussian_orange_list[i - 1], gaussian_extended)
    laplasian_orange_list.append(laplasian)

print(laplasian_apple_list[-1].shape[1])
print(laplasian_apple_list[-1].shape[1])
image = np.hstack((laplasian_apple_list[0][:, :256], laplasian_orange_list[0][:, 256:]))

# New Joined Image Code
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(laplasian_apple_list, laplasian_orange_list):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplasian = np.hstack((apple_lap[:, :int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplasian)

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 7):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow("1", apple_orange_reconstruct)
# cv.imshow("2",laplasian_orange_list[0])
cv.waitKey(0)
cv.destroyAllWindows()
