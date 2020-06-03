import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../Images & Videos/messi5.jpg')
template = img[63:135, 205:263]
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF',
           'cv.TM_SQDIFF_NORMED']

for m in methods:
    img_copy = img.copy()
    topLeft = (0, 0)
    botRight = (0, 0)
    res = cv.matchTemplate(img_copy, template, eval(m))
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)
    if m == 'cv.TM_SQDIFF' or m == 'cv.TM_SQDIFF_NORMED':
        topLeft = minLoc
    else:
        topLeft = maxLoc
    height, width, channels = template.shape
    botRight = (topLeft[0] + width, topLeft[1] + height)
    cv.rectangle(img_copy, topLeft, botRight, (255, 0, 0), 2)
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Heatmap')

    plt.subplot(122)
    plt.imshow(img_copy)
    plt.title('Image')
    plt.show()
