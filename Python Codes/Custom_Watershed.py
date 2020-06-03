import cv2 as cv

import numpy as np

messi = cv.imread('../Images & Videos/messi5.jpg')
messi_copy = messi.copy()
marker_img = np.zeros(messi.shape[:2], dtype=np.int32)
segments = np.zeros(messi.shape, dtype=np.uint8)

n_markers = 10
current_marker = 1
marks_updated = False

# color maps
from matplotlib import cm

colors = []
for i in range(n_markers):
    colors.append(tuple(np.array(cm.tab10(i)[:3]) * 255))


def doThis(event, x, y, flags, params):
    global marks_updated
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(marker_img, (x, y), 10, (current_marker), -1)
        cv.circle(messi_copy, (x, y), 10, colors[current_marker], -1)
        marks_updated = True


cv.namedWindow('messi_img')
cv.setMouseCallback('messi_img', doThis)
while True:
    cv.imshow('Watershed segments', segments)
    cv.imshow('messi_img', messi_copy)
    k = cv.waitKey(1)
    if k == 27:
        break
    # clearing all colors press C
    elif k == ord('c'):
        messi_copy = messi.copy()
        marker_img = np.zeros(messi.shape[:2], dtype=np.int32)
        segments = np.zeros(messi.shape, dtype=np.uint8)
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    if marks_updated:
        marker_img_copy = marker_img.copy()
        mark = cv.watershed(messi, marker_img_copy)
        segments = np.zeros(messi.shape, dtype=np.uint8)
        for color_ind in range(n_markers):
            segments[marker_img_copy == {color_ind}] = colors[color_ind]

cv.destroyAllWindows()
