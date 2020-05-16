# Not Working

import cv2
import numpy as np


def do_nothing(x):
    pass


cap = cv2.VideoCapture(0);

cv2.namedWindow('tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, do_nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, do_nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, do_nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, do_nothing)

while True:
    _, img = cap.read()
    cv2.waitKey(1)
    # img = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if (cv2.waitKey() & 0xFF) == 27:
        break

    LH = cv2.getTrackbarPos('LH', 'tracking')
    LS = cv2.getTrackbarPos('LS', 'tracking')
    LV = cv2.getTrackbarPos('LV', 'tracking')

    UH = cv2.getTrackbarPos('UH', 'tracking')
    US = cv2.getTrackbarPos('US', 'tracking')
    UV = cv2.getTrackbarPos('UV', 'tracking')

    l_b = np.array([LH, LS, LV])
    u_b = np.array([UH, US, UV])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

cap.release()
cv2.destroyAllWindows()
