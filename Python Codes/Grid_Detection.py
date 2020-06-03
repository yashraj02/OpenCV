import cv2 as cv

img = cv.imread('../Images & Videos/chessboard.png')
img = cv.resize(img, (300, 300))
found, corners = cv.findChessboardCorners(img, (7, 7))
print(found)
cv.drawChessboardCorners(img, (7, 7), corners, found)
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
