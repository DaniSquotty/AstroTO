# AstroTO

The repository contains codes we used to extract and analyse ISS images.

## Python programs

* 000_main.py: main program, used no RaspberryPi to make photos on the ISS
* 010_CropImages.py: program that crop images
* 020_ImageMatching.py: program used to match points in different pictures
* 030_StitchImages.py: This code is correct and able to stitching correctly two images considering keypoints
* 040_PixelAnalyses.py: program that convert image in greyscale and calculate the amount of white color in the image. Used to calculate glacier's area
