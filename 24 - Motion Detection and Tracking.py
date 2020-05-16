# first step, movement is difference between two frames
# second, difference has noises because of details and light on video so gaussian blurring is eliminating the noises,
# third, obtaining threshold from clean difference
# fourth, dilating for eliminating district small weak threshold lines which corrupt healthy threshold detection
# fifth, finding contours from clean threshold
# sixth, eliminating small contours which can not be a human by filtering contour area
# seventh, drawing rectangles for each detected contour on the frame, rectangle dimensions obtained from cv2.boundingRect(contour)
# that is it!

import cv2 as cv

cap = cv.VideoCapture('vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
    diff = cv.absdiff(frame1, frame2)
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilate = cv.dilate(threshold, None, iterations=3)
    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 700:
            continue
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame1, 'Status: Movement', (10, 20), cv.FONT_HERSHEY_COMPLEX, 5, (0, 255, 0), 3)
        cv.imshow('1', frame1)
        if (cv.waitKey(40) & 0xFF) == 27:
            break
        frame1 = frame2
        rec, frame2 = cap.read()

cv.destroyAllWindows()
cap.release()
