import cv2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully.")

while cam.isOpened():
    ret, frame = cam.read()
    if ret:
        cv2.imshow('camera', frame)
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break 

cam.release()
cv2.destroyAllWindows()
print("Program ended!")
print("!-~-~-~-~-~-~-!")