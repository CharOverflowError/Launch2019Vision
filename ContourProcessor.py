import cv2
import numpy

class ContourProcessor:
    def __init__(self):
        self.lower = [0, 0, 200]
        self.upper = [10, 10, 255]


    # Pull HSV values from 'values.txt'
    def getHSVBounds(self):
        with open("values.txt", 'r') as f:
            self.lower = [f.readline(), f.readline(), f.readline()]
            self.upper = [f.readline(), f.readline(), f.readline()]

    def findContours(self, frame):
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the BRG image to and HSV for better color detection
        frame_threshold = cv2.inRange(frame, (self.lower[0], self.lower[1], self.lower[2]), (self.upper[0], self.upper[1], self.upper[2]))  # Create a mask for the image based on the HSV color

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

