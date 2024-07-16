import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser(
                    prog='python main.py',
                    description='From a sequence of image files, it creates a single file merged with specified columns and rows, from right to bottom direction')

parser.add_argument('output_filename', help='The output filename with ou without sequence of folders, including file extension')
parser.add_argument('-i', '--files', help='The input files (can have folder and path) without the numbers and without extension. It is expected to start from zero. Ex: ./folder/file_000.png, should put ./folder/file_', required=True)
parser.add_argument('-e', '--extension', default='png', help='The extension of the input files, without de dot(.)', required=True)
parser.add_argument('-d', '--digits', help='The total of digits of numbers to be filled with zeros', required=True, type=int)
parser.add_argument('-c', '--columns', help='The number of columns generated in the output file. The count (colums X rows) have to match the total of files.', required=True, type=int)
parser.add_argument('-r', '--rows', help='The number of rows generated in the output file. The count (colums X rows) have to match the total of files.', required=True, type=int)
parser.add_argument('-cc', '--colorchannels', default=4, help='The number of color channels the input files have. Usually 4 with alpha channels in PNG', type=int)

#input_filename = '/Users/thiago.frensch/Downloads/PNG2/splah_bola_'
#extension = 'png'
#output_file = '/Users/thiago.frensch/Downloads/sprite.png'
#filename_zeros = 5
#columns = 5
#rows = 12
#color_channels = 4
args = parser.parse_args()
print(args.output_filename)
print('-----------')
print(args)

file = args.files + str(0).zfill(args.digits) + "." + args.extension
img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
height = img.shape[0]
width = img.shape[1]

size = height*args.rows, width*args.columns, args.colorchannels
m = np.zeros(size, dtype=np.uint8)
icol = 0
irow = 0
for item in range(0,args.columns*args.rows,1):
	file = args.files + str(item).zfill(args.digits) + "." + args.extension
	print (file) 
	img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
	m[irow*height:irow*height + height, icol*width:icol*width + width] = img
	icol += 1
	if icol >= args.columns :
		icol = 0
		irow += 1
	
cv2.imwrite(args.output_filename, m[:,:,0:args.colorchannels])