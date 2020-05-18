import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def dothis(x):
    pass


cv.namedWindow('trackbar')
# cv.createTrackbar('track1','trackbar',0,255,dothis)
# cv.createTrackbar('track2','trackbar',0,255,dothis)
# while True:
# t1 = cv.getTrackbarPos('track1','trackbar')
# t2 = cv.getTrackbarPos('track2', 'trackbar')
# print(t1, ' ',t2)
# if (cv.waitKey(40) & 0xFF)==27:
#     break
edges = cv.Canny(gray, 25, 80, apertureSize=3)  # 25,80 using trackbar

# ------------------ cv2.HoughLines()--------------------
lines = cv.HoughLines(edges, 1, np.pi / 180,
                      200)  # 200 is threshold: The minimum number of intersections to "*detect*" a line
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow('trackbar', img)

# ------------------ cv2.HoughLinesP()--------------------
img2 = cv.imread('../Images & Videos/sudoku.png')
lines2 = cv.HoughLinesP(edges, 1, np.pi / 180, 200, minLineLength=100, maxLineGap=10)
for line in lines2:
    x1, y1, x2, y2 = line[0]
    cv.line(img2, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imshow('show', img2)
cv.waitKey(0)
cv.destroyAllWindows()
