import cv2 as cv

img = cv.imread('../Images & Videos/chessboard.png')
img = cv.resize(img, dsize=(500, 500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 500, 0.01, 10)
for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, (0, 255, 0), -1)
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
