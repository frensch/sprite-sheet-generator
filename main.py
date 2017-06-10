import numpy as np
import cv2
import math

path_vec = ['walk back', 'walk front', 'walk left', 'walk right', 'walk front left', 'walk front right', 'walk back left', 'walk back right'] 

i = 0
anim_size = 16
total = len(path_vec)*anim_size
print total
columns = int(math.ceil(math.sqrt(total)))
print columns
size = 540*columns, 540*columns, 4
m = np.zeros(size, dtype=np.uint8)
for path in path_vec:
	for item in range(0,16,1):
		# Load an color image in grayscale
		file = path + '/' + ("%04d.png" % (item))
		img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
		print (i%columns)*540
		m[(i//columns)*540:(i//columns)*540 + 540, (i%columns)*540:(i%columns)*540 + 540, 0:columns] = img
		#cv2.imshow('image',m)
		#cv2.waitKey(0)
		i = i + 1
	
m = cv2.resize(m,(1080*2, 1080*2), interpolation = cv2.INTER_CUBIC)
#cv2.imshow('image',m)
#cv2.waitKey(0)
cv2.imwrite('walk.png', m[:,:,0:4])