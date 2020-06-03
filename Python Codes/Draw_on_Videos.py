import cv2 as cv

cap = cv.VideoCapture(0)
top_Left = False
bot_Right = False
x1, y1, x2, y2 = 0, 0, 0, 0


def draw_rect(event, x, y, flag, params):
    global top_Left, bot_Right, x1, y1, x2, y2
    if event == cv.EVENT_LBUTTONDOWN:
        if top_Left and bot_Right:
            x1, y1, x2, y2 = 0, 0, 0, 0
            top_Left = False
            bot_Right = False

        if not top_Left:
            x1, y1 = x, y
            top_Left = True
        elif not bot_Right:
            x2, y2 = x, y
            bot_Right = True


cv.namedWindow('show')
cv.setMouseCallback('show', draw_rect)
while cap.isOpened():
    ret, frame = cap.read()
    if top_Left:
        cv.circle(frame, (x1, y1), 5, (0, 0, 255), 5)
    if top_Left and bot_Right:
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('show', frame)
    cv.waitKey(1)

cap.release()
cv.destroyAllWindows()
