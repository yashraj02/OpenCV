import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
ret, prev_frame = cap.read()
prev_grey = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
prevPts = cv.goodFeaturesToTrack(prev_grey, maxCorners=10, qualityLevel=0.01, minDistance=7, blockSize=7)
mask = np.zeros_like(prev_frame)
while True:
    ret, new_frame = cap.read()
    new_frame_grey = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY)
    nxtPoints, status, error = cv.calcOpticalFlowPyrLK(prev_grey, new_frame_grey, prevPts=prevPoints, nextPts=None,
                                                       winSize=(200, 200), maxLevel=2, criteria=(
        cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    good_new = nxtPoints[status == 1]
    good_prev = prevPoints[status == 1]
    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        mask = cv.line(mask, (x_new, y_new), (x_prev, y_prev), (0, 255, 0), 3)
        new_frame = cv.circle(new_frame, (x_new, y_new), 5, (0, 0, 255), 3)

    img = cv.add(new_frame, mask)
    cv.imshow('tracking', img)
    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break
    prev_grey = new_frame_grey.copy()
    prevPoints = good_new.reshape(-1, 1, 2)
    print(prevPoints, 1, good_new)

cv.destroyAllWindows()
cap.release()
