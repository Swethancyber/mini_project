"""cam.py has two versions of camera code:
   version 1 = shows error messages if camera setup fails
   version 2 = simple, minimal setup
"""
# Version 1

"""import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("error cam")
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        print("error to cap")
        break

    cv2.imshow("cam",frame)
    cv2.waitKey(1) 
cap.release()
cv2.destroyAllWindows()"""

# Version 2 

import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imshow("cam",frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()