import cv2 as cv

img = cv.imread('../Images/sudoku.png', 0)
# img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
img3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow('show1', img)
cv.imshow('show2', img2)
cv.imshow('show3', img3)

cv.waitKey(0)
cv.destroyAllWindows()
