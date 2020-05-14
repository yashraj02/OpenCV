import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(cap.get(3))
print(cap.get(4))

cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        frame = cv2.putText(frame, text, (100, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 5, cv2.LINE_AA)
        # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('My Video Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
