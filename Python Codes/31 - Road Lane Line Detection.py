import cv2 as cv
import numpy as np

img = cv.imread('../Images & Videos/road.jfif')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.resize(img, (500, 500))

w, h = img2.shape[1], img2.shape[0]
region_of_interest_vertices = [
    (0, h), (w / 2, h / 2), (w, h / 2), (w, h)
]


def region_of_interest(image, vertices):
    # Tip: The Bitwise operations should be applied on input image of same dimensions
    mask = np.zeros_like(image)
    # calculates channels 1 for gray & 3 for BGR
    channel_count = image.shape[2]
    # creates (255,255,255)
    match_mask_color = (255,) * channel_count
    # the polygon is filled with white color
    cv.fillPoly(mask, vertices, match_mask_color)
    # using bitwise_and
    # 0(black) and anyvalue = (0)
    # 255(white) and anyvalue = anyvalue
    masked_image = cv.bitwise_and(image, mask)  # Hence the image is replaced in polygon
    return masked_image


cropped_image = region_of_interest(img2, np.array([region_of_interest_vertices], np.int32))
cv.imshow('show', cropped_image)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.imshow(cropped_image)
# plt.show()
