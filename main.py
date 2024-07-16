import numpy as np
import cv2

input_filename = '/Users/thiago.frensch/Downloads/PNG2/splah_bola_'
extension = 'png'
output_file = '/Users/thiago.frensch/Downloads/sprite.png'
filename_zeros = 5
columns = 5
rows = 12
color_channels = 4

file = input_filename + str(0).zfill(filename_zeros) + "." + extension
img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
height = img.shape[0]
width = img.shape[1]

size = height*rows, width*columns, color_channels
m = np.zeros(size, dtype=np.uint8)
icol = 0
irow = 0
for item in range(0,columns*rows,1):
	file = path + filename + str(item).zfill(filename_zeros) + "." + extension
	print (file) 
	img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
	m[irow*height:irow*height + height, icol*width:icol*width + width] = img
	icol += 1
	if icol >= columns :
		icol = 0
		irow += 1
	
cv2.imwrite(output_file, m[:,:,0:color_channels])