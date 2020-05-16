import cv2

img = cv2.imread('../Images/messi5.jpg')
img2 = cv2.imread('../Images/opencv-logo.png')
print(img.shape)

print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
print(b)


def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        str_xy = str(x) + ', ' + str(y)
        print(str(x) + ', ' + str(y))
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, str_xy, (x, y), font, 1, (0, 255, 0), 1)
        cv2.imshow('showing', img)


# ball = img[296:342, 331:390]
# img[273:319, 100:159] = ball
# cv2.imshow('showing',img)
# cv2.setMouseCallback('showing',get_coordinates)
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# img3 = cv2.add(img,img2)
img3 = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
cv2.imshow('showing', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

342, 296
376, 331
