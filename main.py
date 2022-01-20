import cv2
from cvzone.FaceDetectionModule import  FaceDetector

f_detector = FaceDetector()
cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 500)
cap.set(10, 100)


while cap.isOpened():
    _, img = cap.read()
    img, faces = f_detector.findFaces(img)
    print(faces)
    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()