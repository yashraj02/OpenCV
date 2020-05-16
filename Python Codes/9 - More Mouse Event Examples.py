import cv2
import numpy as np

# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('../Images/lena.jpg')
color = np.zeros([512, 512, 3], np.uint8)

event = [i for i in dir(cv2) if 'EVENT' in i]
print(event)
points = []


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        color[:] = [blue, green, red]
        print(color)
        cv2.imshow('color', color)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
            cv2.imshow('Yash', color)
            str_coor = str(x) + ', ' + str(y)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(color, str_coor, (100, 100), font, 1, (0, 255, 0), 3)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (255, 255, 0), 5)
        cv2.imshow('Yash', img)


cv2.imshow('Yash', img)

cv2.setMouseCallback('Yash', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
