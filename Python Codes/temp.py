import cv2 as cv


def empty(x):
    pass


cv.namedWindow("Parameters")
cv.resizeWindow("Parameters", 300, 100)
cv.createTrackbar("Threshold1", "Parameters", 23, 255, empty)
cv.createTrackbar("Threshold2", "Parameters", 20, 255, empty)

img = cv.imread('../Images & Videos/turtleBox3.jpeg')
img = cv.resize(img, (400, 600))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)

while True:
    t1 = cv.getTrackbarPos('Threshold1', 'Parameters')
    t2 = cv.getTrackbarPos('Threshold2', 'Parameters')
    canny = cv.Canny(blur, t1, t2)
    # dilate = cv.dilate(blur,kernel = (5,5),iterations=20)
    cv.imshow('show', canny)
    cv.waitKey(1)
cv.destroyAllWindows()
