import cv2

img = cv2.imread('opencv-logo.png')
cv2.rectangle(img, (0, 200), (400, 50), (255, 0, 0), -1)
cv2.imshow('show', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
