import cv2 as cv

pt = (0, 0)
clicked = False


def drawCircle(event, x, y, flag, param):
    global pt, clicked
    if event == cv.EVENT_LBUTTONDOWN:
        pt = (x, y)
        clicked = True


cv.namedWindow('show')
cv.setMouseCallback('show', drawCircle)
cap = cv.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if clicked:
        cv.circle(frame, pt, 20, (255, 0, 0), 20)
    cv.imshow('show', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()
