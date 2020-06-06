import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
ret, prev_frame = cap.read()
prev_frame_gray = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(prev_frame)
hsv[:, :, 1] = 255

while cap.isOpened():
    ret, new_frame = cap.read()
    new_frame_grey = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prev_frame_gray, new_frame_grey, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitue, angle = cv.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)
    hsv[:, :, 0] = angle / 2
    hsv[:, :, 2] = cv.normalize(magnitue, None, 0, 255, norm_type=cv.NORM_MINMAX)
    img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    cv.imshow('show', img)
    cv.waitKey(10)
    prev_frame_gray = new_frame_grey

cv.destroyAllWindows()
cap.release()
