import cv2
import numpy as np

# img = cv2.imread('lena.jpg',1)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (510, 510), (0, 255, 0), thickness=10)
img = cv2.arrowedLine(img, (0, 255), (255, 200), (0, 255, 0), thickness=10)
img = cv2.rectangle(img, (300, 350), (400, 400), (0, 0, 255), -5)
img = cv2.circle(img, (200, 200), 90, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Yashraj", (10, 500), font, 5, (255, 0, 0), 10, cv2.LINE_AA)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
