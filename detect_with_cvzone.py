import cv2
from cvzone.FaceMeshModule import  FaceMeshDetector

f_detector = FaceMeshDetector(maxFaces=1)
cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 500)
cap.set(10, 100)


while cap.isOpened():
    _, img = cap.read()
    img, faces = f_detector.findFaceMesh(img)
    print(faces)
    cv2.imshow("result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()