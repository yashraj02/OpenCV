import cv2 as cv

cap = cv.VideoCapture(0)
ret, prev_frame = cap.read()
cv.imread('../Images & Videos/haarcascade_frontalface_default.xml')
face_cascade = cv.CascadeClassifier('../Images & Videos/haarcascade_frontalface_default.xml')
face_rectangle = face_cascade.detectMultiScale(prev_frame, scaleFactor=1.2, minNeighbors=5)
print(face_rectangle)
x, y, w, h = face_rectangle[0]
rect = (x, y, w, h)
track_window = rect
roi = prev_frame[y:y + h, x:x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
roi_hist = cv.calcHist([hsv_roi], [0], None, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv.meanShift(dst, track_window, term_criteria)
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv.imshow('img', img2)
        cv.waitKey(1)
cap.release()
cv.destroyAllWindows()
