# Very large variations are observed in intensity when moved in both x & y axis/directions. These variations are detected using harris corner detection.
# Then score R is computed for each window found.
# If R small then its flat region
# If R<0 then its edge (eg edge of square)
# If R large then its a corner.
# Harris Corner requires grayscale images in float format.

import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/chessboard.png')
img = cv.resize(img, dsize=(500, 500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
# for each pixel blocksize=2 means 2*2 neighbourhood is considered
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('dst', img)
cv.waitKey(0)
cv.destroyAllWindows()
