import cv2

img = cv2.imread('../Images & Videos/lena.jpg', 1)

cv2.imshow('This is Lena', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('../Images & Videos/lena_copy.png', img)

# ------------------------------------------------------------------------------------------------
