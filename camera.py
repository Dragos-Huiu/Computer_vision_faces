import cv2
import os

def operate_camera(index):
    cam = cv2.VideoCapture(index)
    os.makedirs(f"camera{index}", exist_ok = True)
    n = 0
    while cam.isOpened():
        ret, frame = cam.read()
        if cv2.waitKey(1) == ord('q') or ret == 0:
            break
        cv2.imshow(f"Camera {index}", frame)
        if cv2.waitKey(1) == ord('s'):
            n += 1
            cv2.imwrite(f"camera{index}\\img{n}.png", frame)
    cv2.destroyAllWindows()
