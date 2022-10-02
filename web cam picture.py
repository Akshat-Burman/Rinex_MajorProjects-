import cv2 

#capturing a particular frame from webcam
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('c'): #by pressing 'c' key on the keyboard it captures the frame from the webcam 
            cv2.imwrite(filename='saved_img.jpg', img=frame)#saving that image
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            break

#face detection        
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#importing haarcascade mode
img = cv2.imread('saved_img.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,9) 

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow('Face Detection',img)#face detected
cv2.waitKey(0)
cv2.destroyAllWindows()
