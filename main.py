import numpy as np
import cv2
import math

path = '/Users/thiago.frensch/Downloads/PNG2'
colordef = 4
columns = 5
rows = 12
width = 360
height = 196
size = height*rows, width*columns, colordef
m = np.zeros(size, dtype=np.uint8)
icol = 0
irow = 0
for item in range(0,60,1):
	file = path + '/splah_bola_' + ("%05d.png" % (item))
	img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
	print (item)
	m[irow*height:irow*height + height, icol*width:icol*width + width] = img
	icol += 1
	if icol >= columns :
		icol = 0
		irow += 1
	#cv2.imshow('image',m)
	#cv2.waitKey(0)
	
cv2.imwrite('sprite.png', m[:,:,0:colordef])