import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../Images & Videos/messi5.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
template = cv.imread('../Images & Videos/messi_face.jpg', 0)
# shape returns (rows, cols) while in an image rows is y axis & col is x axis
h, w = template.shape[:]
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    method = eval(meth)
    res = cv.matchTemplate(gray, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    if meth in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Matching Image')
    plt.xticks(), plt.yticks()
    plt.subplot(122)
    plt.imshow(image)
    plt.title('Detected Image')
    plt.xticks(), plt.yticks()
    plt.suptitle(meth)
    plt.show()
