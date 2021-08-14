import os
import cv2
import time

vc = cv2.VideoCapture(0)
img_counter = 0

while(True):
    ret, frame = vc.read()

    window_name = "PY Cam by DW"
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (30, 30)
    fontScale = 0.7
    color = (255, 0, 0)
    thickness = 1

    frame = cv2.putText(frame, "Press 'Spacebar' to take Image", org, font, fontScale, color, thickness, cv2.LINE_AA)

    font2 = cv2.FONT_HERSHEY_SIMPLEX
    org2 = (30, 55)
    fontScale2 = 0.7
    color2 = (255, 0, 0)
    thickness2 = 1

    frame = cv2.putText(frame, "Press 'ESC' to Exit", org2, font2, fontScale2, color2, thickness2, cv2.LINE_AA)

    cv2.imshow(window_name, frame)

    if not ret:
        break

    k = cv2.waitKey(1)

    if k%256 == 32:
        ret, frame = vc.read()
        path = "C:\Bilder"
        img_name=("opencv_frame_{}.png".format(img_counter))
        cv2.imwrite(os.path.join(path,img_name),frame)
        img_counter += 1
        print("{} written!".format(img_counter))
        time.sleep(1.5)


    if k%256 == 27:
        break

vc.release()
cv2.destroyAllWindows()

