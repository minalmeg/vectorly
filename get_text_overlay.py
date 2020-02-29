# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
     
    image = cv2.imread('C:/Users/Minal/Desktop/simpsons_frame0.png')
    coefficients = [10,10,10]
    m = np.array(coefficients).reshape((1,3))
    blue = cv2.transform(image, m)
    width = int(blue.shape[1] * 60 / 100)
    height = int(blue.shape[0] * 60 / 100)
    dim = (width, height)
    output = cv2.resize(blue, dim, interpolation = cv2.INTER_AREA)

    return output

if __name__ == '__main__':
    image = cv2.imread('C:/Users/Minal/Desktop/simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imshow('simpons_text.png', output)
#####################

