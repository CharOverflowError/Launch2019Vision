import cv2
import numpy
from Camera import Camera
from ContourProcessor import ContourProcessor
from TargetFinder import TargetFinder
import VideoStreamer

# Initialize all processing classes and cameras
camera = Camera(0)
contourProc = ContourProcessor()
targetFinder = TargetFinder()

# Setup the video stream
VideoStreamer.setCamera(camera)
VideoStreamer.run()



# while(camera.cap.isOpened()):
#     ret, frame = camera.cap.read()  # Capture the frame for processing
    
#     if ret == True:
#         contours = contourProc.findContours(frame)

#         boundingRects = []
#         if len(contours) > 0:
#             for contour in contours:
#                 rect = contourProc.getBoundingRect(contour)
#                 boundingRects.append(rect)

#                 # box = cv2.boxPoints(rect)
#                 # box = numpy.int0(box)

#                 # boundingBoxes.append(box)

#             boundingRects = targetFinder.filterRectsByRatio(boundingRects)

#             boundingBoxes = []
#             if len(boundingRects) > 0:
#                 for rect in boundingRects:
#                     box = cv2.boxPoints(rect)
#                     box = numpy.int0(box)
#                     boundingBoxes.append(box)

            
#             cv2.drawContours(frame, boundingBoxes, 0,(0,0,255),2)

#         # # Display the resulting masked image
#         # cv2.imshow('Frame', frame)

#         # Press Q on keyboard to  exit
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

    # # Break the loop
    # else:
    #     break

        
