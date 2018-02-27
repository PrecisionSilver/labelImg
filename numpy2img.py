import numpy as np
import argparse
from scipy.misc import imsave

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='convert numpy ndarray to images')
	parser.add_argument('-i', type = str, help = 'The input file name.')
	parser.add_argument('-o', type = str, help = 'output path')
	parser.add_argument('--base-num', type = int, default = 0, help = 'file name start number')
	parser.add_argument('--image-type', type = str, defult = 'tif', help = 'image file type')

	args = parser.parse_args()

	images = np.load(args.i)

	for i in range(len(images)):
		imsave('%s%d.%s' % (args.o, args.base_num + i, args.image_type), images[i])

