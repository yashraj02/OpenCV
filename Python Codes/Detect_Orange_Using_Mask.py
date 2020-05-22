# finding orange using mask
import cv2 as cv
import numpy as np


def dothis(x):
    pass


cv.namedWindow('trackbar')
cv.createTrackbar('LH', 'trackbar', 0, 255, dothis)
cv.createTrackbar('LS', 'trackbar', 255, 255, dothis)
cv.createTrackbar('LV', 'trackbar', 255, 255, dothis)
cv.createTrackbar('HH', 'trackbar', 0, 255, dothis)
cv.createTrackbar('HS', 'trackbar', 255, 255, dothis)
cv.createTrackbar('HV', 'trackbar', 255, 255, dothis)
img = cv.imread('../Images & Videos/apple.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
while True:
    t1 = cv.getTrackbarPos('LH', 'trackbar')  #
    t2 = cv.getTrackbarPos('LS', 'trackbar')  # 255
    t3 = cv.getTrackbarPos('LV', 'trackbar')  # 0
    t4 = cv.getTrackbarPos('HH', 'trackbar')  # 180
    t5 = cv.getTrackbarPos('HS', 'trackbar')  # 255
    t6 = cv.getTrackbarPos('HV', 'trackbar')  # 90
    # print(t1,t2,t3,t4,t5,t6)
    # mask = cv.inRange(hsv,(t1, t2, t3),(t4, t5, t6))
    mask = cv.inRange(hsv, (0, 0, 0), (21, 255, 255))
    img2 = cv.bitwise_and(img, img, mask=mask)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, img2])
    hstack = cv.resize(hstack, (750, 350))
    cv.imshow('show', hstack)
    cv.waitKey(1)
