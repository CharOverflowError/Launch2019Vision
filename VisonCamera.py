# import cv2
# import numpy
# from threading import Thread


# class VisionCamera:
#     def __init__(self, num):
#         self.num = num

#         self.lower = [0, 0, 0]
#         self.upper = [255, 255, 255]

#         # thread = Thread(target=self.process_stream)
#         # thread.run()

#         self.process_stream()

#     def process_stream(self):

#         self.capture = cv2.VideoCapture(self.num)

#         # Read until video is completed
#         while (self.capture.isOpened()):
#             # Capture frame-by-frame
#             ret, frame = self.capture.read()
#             if ret == True:

#                 frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#                 self.get_HSV_bounds()

#                 frame_threshold = cv2.inRange(frame, (self.lower[0], self.lower[1], self.lower[2]), (self.upper[0], self.upper[1], self.upper[2]))

#                 contours, hierarchy = cv2.findContours(frame_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#                 if contours:
#                     matches = self.findTarget(contours, frame)

#                 # Mask the original image
#                 masked = cv2.bitwise_and(frame, frame, mask=frame_threshold)

#                 # Display the resulting masked image
#                 cv2.imshow('Masked', frame)

#                 # Press Q on keyboard to  exit
#                 if cv2.waitKey(25) & 0xFF == ord('q'):
#                     break

#             # Break the loop
#             else:
#                 break

#         # When everything done, release the video capture object
#         self.capture.release()

#         # Closes all the frames
#         cv2.destroyAllWindows()

#     def changeColor(self, lower, upper):
#         self.lower = lower
#         self.upper = upper

#     def get_HSV_bounds(self):
#         with open("values.txt", "r") as f:
#             try:
#                 hmin = int(f.readline().strip("\n"))
#                 smin = int(f.readline().strip("\n"))
#                 vmin = int(f.readline().strip("\n"))
#                 hmax = int(f.readline().strip("\n"))
#                 smax = int(f.readline().strip("\n"))
#                 vmax = int(f.readline().strip("\n"))

#                 self.lower = [hmin, smin, vmin]
#                 self.upper = [hmax, smax, vmax]

#             except ValueError:
#                 print("Lower and upper HSV bounds could not be read. Skipping bound check")


#     def findTarget(self, contours, frame):
#         matches = []
#         for contour in contours:
#             if type(contour) != int:
#                 (x, y, w, h) = cv2.boundingRect(contour)
#                 if w > 20 and h > 20:
#                     if round((w / h) * 5) == round((7 / 12) * 5):
#                         matches.append(contour)
#                         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         cv2.drawContours(frame, matches, -1, (0, 255, 0), 3)
#         return matches
