from PIL import Image
import cv2
import numpy as np
import glob
import os

NAME = "baroque"
MIN_SIZE = 350

os.mkdir("./processed-images/" + NAME)

i = 0
for filename in glob.glob("./images/" + NAME + "/*.jpg"):
	# Load img
	image = np.array(Image.open(filename))

	# Filter out non RGB images
	if len(image.shape) != 3 or image.shape[2] != 3:
		continue

	# Filter out if too small
	if image.shape[0] < MIN_SIZE or image.shape[1] < MIN_SIZE:
		continue

	tmp = cv2.resize(image, (int(1024), int(1024)), interpolation=cv2.INTER_CUBIC)
	im = Image.fromarray(tmp)
	im.save("./processed-images/" + NAME + "/" + str(i) + ".jpg")
	i += 1