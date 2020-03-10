#!/bin/bash

rsync --exclude '*pkl' -avz -e ssh uqfcogno@wiener.hpc.net.uq.edu.au:/scratch/cai/GAN/results/000-pgancubism-preset-v2-1gpu-fp32/ \
	results/002-pganabstract-preset-v2-1gpu-fp32
