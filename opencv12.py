import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')


def do_this(X):
    print(X)


cv2.createTrackbar('B', 'image', 0, 255, do_this)
cv2.createTrackbar('G', 'image', 0, 255, do_this)
cv2.createTrackbar('R', 'image', 0, 255, do_this)
cv2.createTrackbar('switch', 'image', 0, 1, do_this)

while (1):
    cv2.imshow('image', img)
    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    cv2.waitKey(1)
    B = cv2.getTrackbarPos('B', 'image')
    G = cv2.getTrackbarPos('G', 'image')
    R = cv2.getTrackbarPos('R', 'image')
    switch = cv2.getTrackbarPos('switch', 'image')
    if switch == 0:
        img[:] = 0
    else:
        img[:] = [B, G, R]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
