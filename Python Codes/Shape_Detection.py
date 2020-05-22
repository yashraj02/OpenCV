import cv2 as cv

cv.namedWindow('track')
cv.resizeWindow('track', 400, 100)


def doThis(x):
    pass


cv.createTrackbar('t1', 'track', 15, 300, doThis)
cv.createTrackbar('t2', 'track', 216, 300, doThis)
img = cv.imread('../Images & Videos/turtleBox3.jpeg')
img = cv.resize(img, (300, 400))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)
while True:
    t1 = cv.getTrackbarPos('t1', 'track')
    t2 = cv.getTrackbarPos('t2', 'track')
    canny = cv.Canny(blur, t1, t2)
    dilated = cv.dilate(canny, (7, 7))
    contours, hierarchy = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # for cnt in contours:
    cv.drawContours(img, contours, -1, (0, 255, 0), 1)
    cv.imshow('show1', img)
    cv.waitKey(1)
cv.destroyAllWindows()
