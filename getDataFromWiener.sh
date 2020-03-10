#!/bin/bash

#rsync --exclude '*pkl' -avz -e ssh s4559398@wiener.hpc.net.uq.edu.au:/scratch/cai/progressive_growing_of_gans/results/000-pganmelanoma-preset-v2-1gpu-fp32/ \
#	results/000-pganmelanoma-preset-v2-1gpu-fp32

#rsync --exclude '*pkl' -avz -e ssh s4559398@wiener.hpc.net.uq.edu.au:/scratch/cai/progressive_growing_of_gans/results/001-pgannevus-preset-v2-1gpu-fp32/ \
#	results/001-pgannevus-preset-v2-1gpu-fp32

rsync --exclude '*pkl' -avz -e ssh s4559398@wiener.hpc.net.uq.edu.au:/scratch/cai/progressive_growing_of_gans/results/002-pganabstract-preset-v2-1gpu-fp32/ \
	results/002-pganabstract-preset-v2-1gpu-fp32

rsync --exclude '*pkl' -avz -e ssh s4559398@wiener.hpc.net.uq.edu.au:/scratch/cai/progressive_growing_of_gans/results/003-pganlandscapes-preset-v2-1gpu-fp32/ \
	results/003-pganlandscapes-preset-v2-1gpu-fp32

rsync --exclude '*pkl' -avz -e ssh s4559398@wiener.hpc.net.uq.edu.au:/scratch/cai/progressive_growing_of_gans/results/004-pganself-portrait-preset-v2-1gpu-fp32/ \
	results/004-pganself-portrait-preset-v2-1gpu-fp32
