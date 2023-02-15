
# Importing the required libraries
import cv2
import numpy as np
import dlib
  
  
# Connect your pcs camera
capture = cv2.VideoCapture(0)
  
  
# Detect the coordinates of the faces
detector = dlib.get_frontal_face_detector()
  
  
# Capture the frames simultaneously

while True:
  
    # Capturing continously
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
  
    # Convert RGB to grayscale to pick coordinates
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
  
    # Iterator to count the number of faces
    i = 0
    for face in faces:
  
        # Get the coordinates of faces detected
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
  
        # Increment iterator for each face detected in faces
        i = i+1
  
        # Display the box and the faces detected
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(face, i)
  
    # Display the resulted frame
    cv2.imshow('frame', frame)
  
    # Exit the program with the "E" button on a keyboard.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
  
# End the capture and close the windows
capture.release()
cv2.destroyAllWindows()