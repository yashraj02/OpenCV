# Detecting edges
# 5 steps:
# Noise Reduction - Gaussian Filter to smooth image
# Gradient Calculation - find intensity/color gradiance
# Non Maximum Supression - get rid of spurious response while edge detection
# Double Threshold - to determine potential edges
# Edge Tracking by Hysteresis - supress all other weak edges

import cv2 as cv


def nothing(x):
    pass


cv.namedWindow('track')
cv.createTrackbar('track1', 'track', 0, 500, nothing)
cv.createTrackbar('track2', 'track', 0, 500, nothing)

img = cv.imread('../Images & Videos/messi5.jpg', 0)

while True:
    t1 = cv.getTrackbarPos('track1', 'track')
    print(t1)
    t2 = cv.getTrackbarPos('track2', 'track')
    print(t2)
    canny = cv.Canny(img, t1, t2)
    cv.imshow('show', canny)

    if (cv.waitKey(1) & 0xFF) == 27:
        break

cv.destroyAllWindows()
