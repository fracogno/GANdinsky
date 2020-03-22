import pickle
import numpy as np
import tensorflow as tf
import PIL.Image

# Initialize TensorFlow session.
tf.InteractiveSession()

# Variables
TOTAL = 0
ckps = ["000-pgancubism-preset-v2-1gpu-fp32", "001-pganself-portrait-preset-v2-1gpu-fp32", "002-pganbaroque-preset-v2-1gpu-fp32"]
imagesToGenerate = 50

for ckp in ckps:
	for epoch in range(10500, 12001, 100):
		# Import official networks
		with open('./results/' + ckp + '/network-snapshot-0' + str(epoch) + '.pkl', 'rb') as file:
		    G, D, Gs = pickle.load(file)

		# Generate latent vectors.
		latents = np.random.randn(imagesToGenerate, *Gs.input_shapes[0][1:])

		# Generate dummy labels (not used by the official networks).
		labels = np.zeros([latents.shape[0]] + Gs.input_shapes[1][1:])

		# Run the generator to produce a set of images.
		images = Gs.run(latents, labels)

		# Convert images to PIL-compatible format.
		images = np.clip(np.rint((images + 1.0) / 2.0 * 255.0), 0.0, 255.0).astype(np.uint8) # [-1,1] => [0,255]
		images = images.transpose(0, 2, 3, 1) # NCHW => NHWC

		# Save images as PNG.
		for idx in range(images.shape[0]):
		    PIL.Image.fromarray(images[idx], 'RGB').save('./generated/' + str(TOTAL) + '.png')
		    TOTAL += 1