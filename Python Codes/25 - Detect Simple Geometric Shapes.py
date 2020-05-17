import cv2 as cv

img = cv.imread('../Images & Videos/shapes.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# For determining threshold
# def dothis(x):
#     pass
# cv.namedWindow('image')
# cv.createTrackbar('L','image',0,255,dothis)
# cv.createTrackbar('H','image',0,255,dothis)

def detect(c):
    shape = 'Unidentified'
    # Contour Approximation
    epsilon = cv.arcLength(c, True)
    print(epsilon)
    approx = cv.approxPolyDP(c, 0.04 * epsilon, True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    print(approx)
    if len(approx) == 3:
        shape = 'Triangle'
    elif len(approx) == 4:
        # compute the bounding box of the contour and use the
        # bounding box to compute the aspect ratio
        x, y, w, h = cv.boundingRect(approx)
        ar = w / float(h)
        shape = 'Square' if ar >= 0.95 and ar <= 1.05 else 'Rectangle'
    elif len(approx) == 5:
        shape = 'Pentagon'
    elif len(approx) == 10:
        shape = 'Star'
    else:
        shape = 'Circle'
    return shape, x, y - 7


# while True:
# L = cv.getTrackbarPos('L','image')
# H = cv.getTrackbarPos('H', 'image')
_, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 0, 0), 2)
for c in contours:
    shape, x, y = detect(c)
    cv.putText(img, shape, (x, y), cv.FONT_HERSHEY_COMPLEX, 0.3, (0, 255, 0), 1)

cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
