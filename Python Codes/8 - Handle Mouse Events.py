import cv2

# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('../Images & Videos/lena.jpg')

event = [i for i in dir(cv2) if 'EVENT' in i]
print(event)

points = []


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 2, (x, y, x), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (255, 255, 0), 5)
        cv2.imshow('Yash', img)


cv2.imshow('Yash', frame)

cv2.setMouseCallback('Yash', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
