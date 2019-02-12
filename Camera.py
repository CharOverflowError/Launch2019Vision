import cv2
import os

class Camera:
    def __init__(self, port):
        self.port = port
        self.cap = cv2.VideoCapture(port)

    def getMJPEG(self):
        success, frame = self.cap.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def setBrightness(value):
        os.system("v4l2-ctl -d /dev/video{} --set-ctrl=brightness={}".format(self.port, value))
