import cv2


def do_this(x):
    print(x)


cv2.namedWindow('image')
cv2.createTrackbar('num', 'image', 0, 500, do_this)
cv2.createTrackbar('grey_scale', 'image', 0, 1, do_this)

while (1):
    img = cv2.imread('lena.jpg')
    pos = cv2.getTrackbarPos('num', 'image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (100, 100), font, 2, (0, 255, 0), 2)

    grey_flag = cv2.getTrackbarPos('grey_scale', 'image')
    if grey_flag == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if (cv2.waitKey(1) & 0xFF) == 27:
        break
    img = cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
