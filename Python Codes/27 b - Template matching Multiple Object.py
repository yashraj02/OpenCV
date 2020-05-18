import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/landscape.jfif')
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('../Images & Videos/landscape2.jfif', 0)
h, w = template.shape
res = cv.matchTemplate(img2, template, cv.TM_CCOEFF_NORMED)
threshold = 0.1
loc = np.where(res >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
cv.imshow('show', img)
cv.waitKey(0)

# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img_rgb = cv.imread('../Images & Videos/landscape.jfif')
# img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
# template = cv.imread('../Images & Videos/landscape2.jfif',0)
# w, h = template.shape[::-1]
# res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#
# cv.imshow('show',img_rgb)
# cv.waitKey(0)
# cv.destroyAllWindows()
