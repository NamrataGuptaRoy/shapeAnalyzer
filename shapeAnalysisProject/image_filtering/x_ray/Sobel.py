'''The following code is taken from the documentation of scipy's
implementation of Sobel's Edge Detection method
'''

from scipy import ndimage
import numpy as np
# Matplotlib is imported during development phase only
#from matplotlib import pyplot as plt

def filter_image(input_vector, percentile=95):
    print "Executing Phase 2: Edge Detection Sobel's Algorithm"
#    plt.imshow(input_vector)
#    plt.show()
    dx = ndimage.sobel(input_vector, 0) # derivative in x direction
    dy = ndimage.sobel(input_vector, 1) # derivative in y direction
    mag = np.hypot(dx, dy)
    result = np.zeros_like(mag)
    result[mag>np.percentile(mag, percentile)] = 1
#    plt.imshow(result)
#    plt.show()
    return result
