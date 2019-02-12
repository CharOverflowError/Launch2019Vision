import cv2

class TargetFinder:
    def __init__(self):
        self.contours = []

    # def findTarget(self, boundingRects):
    #     for boundingRect in boundingRects:

    def filterRectsByRatio(self, boundingRects):
        goodRects = []
        for boundingRect in boundingRects:
            if round(boundingRect[0][0] / boundingRect[0][1] * 10) == 0.5:  # TODO: get actual ratio of width to height
                goodRects.append(boundingRect)

        return goodRects

    def filterRectsByFullness(self, boundingRects):
        goodRects = []
        for boundingRect in boundingRects:
            if round(boundingRect[2] / 10) == 12:  # TODO: get actual angle of target
                goodRects.append(boundingRect)

        return goodRects