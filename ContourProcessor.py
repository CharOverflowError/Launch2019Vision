import cv2
import numpy
from threading import Lock
import math

class ContourProcessor:
    def __init__(self):
        self.lower = [0, 0, 100]
        self.upper = [100, 100, 255]
        self.boundingRects = []
        self.boudningBoxes = []


    # Pull HSV values from 'values.txt'
    def getHSVBounds(self):
        print("Updating HSV bounds")
        with open("values.txt", 'r') as f:
            self.lower = [int(f.readline()), int(f.readline()), int(f.readline())]
            self.upper = [int(f.readline()), int(f.readline()), int(f.readline())]

    def getThreshold(self, frame):
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert the BRG image to and HSV for better color detection
        return cv2.inRange(frame_HSV, (self.lower[0], self.lower[1], self.lower[2]), (self.upper[0], self.upper[1], self.upper[2]))  # Create a mask for the image based on the HSV color

    def findContours(self, frame):
        frame_threshold = self.getThreshold(frame)

        contours, hierarchy = cv2.findContours(frame_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Draw bounds around the desired color
        contours = self.filterContours(contours)
        
        return contours
    
    # Filter contour list to prevent blatantly obvious false positives
    def filterContours(self, contours):
        goodContours = []

        if len(contours) > 0:
            for contour in contours:
                ((x, y), (w, h), angle) = self.getBoundingRect(contour)
                
                if w > 20 and h > 20:
                    goodContours.append(contour)

        return goodContours

    def getBoundingRect(self, contour):
        rect = cv2.minAreaRect(contour)
        return rect

    def drawBoundingBoxes(self, contours, frame):
        self.boundingRects = []
        for contour in contours:
            self.boundingRects.append(self.getBoundingRect(contour))

        self.boundingBoxes = []
        if len(self.boundingRects) > 0:
            for rect in self.boundingRects:
                box = cv2.boxPoints(rect)
                box = numpy.int0(box)
                self.boundingBoxes.append(box)

        cv2.drawContours(frame, self.boundingBoxes, -1,(0,0,255),2)

        return frame

    def drawCenterLine(self, frame):
        height, width, channels = frame.shape
        color = (0, 0, 255) # Red
        
        for boundingBox in self.boundingBoxes:
            min_x = width
            max_x = 0
            for corner in boundingBox:
                if corner[0] < min_x:
                    min_x = corner[0]
                elif corner[0] > max_x:
                    max_x = corner[0]

            if round(width / 2) >= min_x and round(width / 2) <= max_x:
                color = (0, 255, 0)  # Green

        cv2.line(frame, (round(width / 2), round(height / 4)), (round(width / 2), round(height - (height / 4))), color, 2)

