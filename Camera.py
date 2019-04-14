import cv2
import os
import numpy as np
from threading import Thread
from PIL import Image
import io

class Camera:
    def __init__(self, port):
        self.port = port
        self.cap = cv2.VideoCapture(port)
        self.latestFrame = np.zeros([480,640,3], dtype=np.uint8)
        self.latestFrame[:,0:320] = (255,0,0)      # (B, G, R)
        self.latestFrame[:,320:640] = (0,255,0)
        self.latestProcessedFrame = np.zeros([480,640,3], dtype=np.uint8) #  Create empty frame

    def getMJPEGProcessedFrame(self):
        param = [int(cv2.IMWRITE_JPEG_QUALITY), 15]
        ret, jpeg = cv2.imencode('.jpg', self.latestProcessedFrame, param)
        if ret:
            return jpeg.tobytes()


    def setBrightness(self, value):
        os.system("v4l2-ctl -d /dev/video{} --set-ctrl=brightness={}".format(self.port, value))

    def setProcessedFrame(self, frame):
        self.latestProcessedFrame = frame

    def connected(self):
        ret, frame = self.cap.read()
        if self.cap.isOpened():
            return True
        return False

    def getFrames(self):
        while Thread.is_alive:
            ret, frame = self.cap.read()
            if ret:
                self.latestFrame = frame

    def startCap(self):
        self.capThread = Thread(target=self.getFrames).start()

    def stopCap(self):
        if self.capThread:
            self.capThread.stop()
