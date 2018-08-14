import numpy as np
import cv2
import cv2.aruco as aruco

# marker bit arrays
bit_arrays = np.array([
			    	   # marker-0
					   [[1, 0, 1, 1, 0],
   					    [1, 0, 0, 0, 1],
   					    [0, 0, 1, 1, 0],
   					    [1, 1, 1, 1, 0],
   					    [1, 0, 1, 0, 0]],
   					   # marker-1
   					   [[1, 0, 0, 0, 0],
   					    [0, 0, 0, 0, 0],
   					    [0, 1, 0, 1, 1],
   					    [1, 0, 1, 1, 1],
   					    [0, 1, 1, 1, 1]],
   					   # marker-2
   					   [[1, 1, 1, 0, 0],
   					    [0, 1, 1, 1, 1],
   					    [1, 0, 0, 0, 0],
   					    [0, 1, 1, 1, 1],
   					    [1, 1, 1, 1, 0]],
   					   # marker-3
   					   [[0, 0, 0, 0, 0],
   					    [1, 0, 0, 1, 1],
   					    [0, 1, 1, 0, 0],
   					    [0, 1, 1, 0, 0],
   					    [0, 0, 0, 1, 1]]
   				      ], dtype='uint8')

def createDict():
	# creates dictionary of markers based on marker bit arrays
	markers = aruco.Dictionary_create(bit_arrays.shape[0], bit_arrays.shape[1])
	byte_arrays = []
	for array in bit_arrays:
		byte_arrays.append(aruco.Dictionary_getByteListFromBits(array))
	bytesList = np.concatenate(byte_arrays, 0)
	markers.bytesList = bytesList
	return markers
 
markers = createDict()
for i in xrange(0, 4):
  img = aruco.drawMarker(markers, i, 800)
  cv2.imwrite("markers/marker-" + str(i) + ".png", img)
