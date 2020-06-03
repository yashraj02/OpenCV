import cv2 as cv

# p_img -> parent Image
# c_img -> child Image
p_img = cv.imread('../Images & Videos/messi5.jpg')
c_img = cv.imread('../Images & Videos/OpenCV_Logo_white.png')
c_img = cv.resize(c_img, (200, 200))
c_img_grey = cv.cvtColor(c_img, cv.COLOR_BGR2GRAY)

roi = p_img[0:c_img.shape[0], 0:c_img.shape[1]]
ret, c_mask = cv.threshold(c_img_grey, 150, 255, cv.THRESH_BINARY)  # background is white logo is black
# Black the logo area in roi
roi = cv.bitwise_and(roi, roi, mask=c_mask)

c_mask = cv.bitwise_not(c_mask)  # inversing we get white logo black background
# take only region of logo in logo image
c_color_mask = cv.bitwise_and(c_img, c_img, mask=c_mask)
# add logo in ROI & modify img
dst = cv.add(roi, c_color_mask)
p_img[0:c_img.shape[0], 0:c_img.shape[1]] = dst
cv.imshow('p_img', c_mask)
cv.waitKey(0)
cv.destroyAllWindows()
