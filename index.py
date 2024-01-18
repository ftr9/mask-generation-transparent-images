import cv2
import numpy as np
import os

from glob import glob

path = r"C:\Users\asus\Desktop\generateGGrayScale\transparentimages"


for image_path in glob(os.path.join(path, "images", "*")):
    
    image = cv2.imread(image_path)

# Assuming that the removed background is black in the image
# You may need to adjust this based on your specific case
    binary_mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary_mask = cv2.threshold(binary_mask, 1, 255, cv2.THRESH_BINARY)

    inverted_mask = cv2.bitwise_not(binary_mask)
    
    # Get the base name (filename with extension)
    base_name = os.path.basename(image_path)

    # Split the base name into the name and extension
    image_name, extension = os.path.splitext(base_name)

    cv2.imwrite(f"transparentimages/masks/{image_name}.png", inverted_mask)
    
    


    

'''
# Load the image from which the background is removed
image = cv2.imread('samplle.png')

# Assuming that the removed background is black in the image
# You may need to adjust this based on your specific case
binary_mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_mask = cv2.threshold(binary_mask, 1, 255, cv2.THRESH_BINARY)

inverted_mask = cv2.bitwise_not(binary_mask)

cv2.imwrite('ground_truth_mask.png', inverted_mask)
'''