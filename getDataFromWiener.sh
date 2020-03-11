#!/bin/bash
rsync --exclude '*pkl' -avz -e ssh uqfcogno@wiener.hpc.net.uq.edu.au:/scratch/cai/GAN/results/*	results/