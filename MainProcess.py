import cv2
import numpy
from Camera import Camera
from ContourProcessor import ContourProcessor
from TargetFinder import TargetFinder
import VideoStreamer
from threading import Thread


camera = Camera(1)
contourProc = ContourProcessor()
targetFinder = TargetFinder()

def worker():
    while Thread.is_alive:
        # # Capture frame-by-frame
        # ret, frame = camera.cap.read()

        # if ret == True:
        #     contours = contourProc.findContours(frame)

        #     boundingRects = []
        #     if len(contours) > 0:
        #         for contour in contours:
        #             rect = contourProc.getBoundingRect(contour)
        #             boundingRects.append(rect)

        #             # box = cv2.boxPoints(rect)
        #             # box = numpy.int0(box)

        #             # boundingBoxes.append(box)

        #         # boundingRects = targetFinder.filterRectsByRatio(boundingRects)

        #         boundingBoxes = []
        #         if len(boundingRects) > 0:
        #             for rect in boundingRects:
        #                 box = cv2.boxPoints(rect)
        #                 box = numpy.int0(box)
        #                 boundingBoxes.append(box)

                
        #         cv2.drawContours(frame, boundingBoxes, 0,(0,0,255),2)


        #     # # Display the resulting masked image
        contours = contourProc.findContours(camera.latestFrame)
        masked = cv2.bitwise_and(camera.latestFrame, camera.latestFrame, mask=contourProc.getThreshold(camera.latestFrame))
        latestProcFrame = contourProc.drawBoundingBoxes(contours, masked)
        contourProc.drawCenterLine(latestProcFrame)  # Visual to show if robot is centered on target or not
        camera.setProcessedFrame(latestProcFrame)

if camera.connected():
    camera.startCap()

    # Start a thread for the frame processing
    proc_thread = Thread(target=worker).start()

    # Setup the video stream
    VideoStreamer.setCamera(camera)
    VideoStreamer.setContourProcessor(contourProc)
    VideoStreamer.run()
else:
    print("Camera is not connected")
