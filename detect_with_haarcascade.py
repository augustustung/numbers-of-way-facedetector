# nhan dien khuon mat
import cv2

path = 'resource/anh_the_trang.jpg'
faceCascade = cv2.CascadeClassifier('resource/haarcascade_fontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 500)
cap.set(10, 100)

while cap.isOpened():
    _, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()