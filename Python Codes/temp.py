# import numpy as np
# import cv2 as cv
#
# img = cv.imread('../Images & Videos/turtleBox3.jpeg',-1)
# img = cv.resize(img,(300,400))
# rgb = cv.split(img)
# print(rgb)
# print(img.shape)
# cv.imshow('show',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import cv2
# import numpy as np
# new = []
# image = cv2.imread("../Images & Videos/shadowed_paper.jpg", 0)
# if sum(image[0]) / len(image[0]) < 200:
#     new = np.where((255 - image) < image, 255, image * 2)
# else:
#     new = image
# cv2.imshow('show',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

new = []
image = cv2.imread("../Images & Videos/Heart_10x10.png")
r, g, b = cv2.split(image)
print(image.shape)
print(image[0][0])
cv2.imshow('show', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
