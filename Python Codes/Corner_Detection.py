# Corner Harris
import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/chessboard.png')
img = cv.resize(img, (300, 300))
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img_grey = np.float32(img_grey)
# dst = cv.cornerHarris(img_grey,blockSize=2,ksize=3,k=0.04)
# dst = cv.dilate(dst,None)
# img[dst>0.01*dst.max()] = [255,0,0] #Thresholding
# plt.imshow(img)
# plt.show()
# cv.imshow('show',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Shi Tomasi
corners = cv.goodFeaturesToTrack(img_grey, 100, 0.01, 10)
corners = np.int0(corners)
for c in corners:
    x, y = c.ravel()
    cv.circle(img, (x, y), 2, (0, 0, 255), 2)
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
