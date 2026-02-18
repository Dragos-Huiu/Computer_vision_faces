import cv2

def operate_camera(index):
    cam = cv2.VideoCapture(index)
    while cam.isOpened():
        ret, frame = cam.read()
        if cv2.waitKey(1) == ord('q') or ret == 0:
            break
        cv2.imshow(f"Camera {index}", frame)
    cv2.destroyAllWindows()
