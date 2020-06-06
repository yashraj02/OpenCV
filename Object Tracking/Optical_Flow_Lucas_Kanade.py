import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
ret, prev_frame = cap.read()
prev_frame_grey = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
prev_pts = cv.goodFeaturesToTrack(prev_frame_grey, maxCorners=10, qualityLevel=0.03, minDistance=5, blockSize=7)
mask = np.zeros_like(prev_frame)
while True:
    ret, new_frame = cap.read()
    new_frame_grey = cv.cvtColor(new_frame, cv.COLOR_BGR2GRAY)
    new_pts, status, err = cv.calcOpticalFlowPyrLK(prev_frame_grey, new_frame_grey, prevPts=prev_pts, nextPts=None,
                                                   winSize=(200, 200), maxLevel=2,
                                                   criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    goodprev = prev_pts[status == 1]
    goodnew = new_pts[status == 1]
    for i, (prev, new) in enumerate(zip(goodprev, goodnew)):
        x_prev, y_prev = prev.ravel()
        x_new, y_new = new.ravel()
        mask = cv.line(mask, (x_new, y_new), (x_prev, y_prev), (0, 255, 0), 2)
        new_frame = cv.circle(new_frame, (x_new, y_new), 5, (0, 0, 255), 3)

    frame = cv.add(new_frame, mask)
    cv.imshow('show', frame)
    cv.waitKey(30)
    prev_frame_grey = new_frame_grey.copy()
    prev_pts = goodnew.reshape(-1, 1, 2)

cv.destroyAllWindows()
cap.release()
