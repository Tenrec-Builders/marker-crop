import numpy as np
import cv2
import cv2.aruco as aruco
 
 
markers = aruco.Dictionary_create(4, 5)
for i in xrange(0, 4):
  img = aruco.drawMarker(markers, i, 800)
  cv2.imwrite("markers/marker-" + str(i) + ".png", img)
