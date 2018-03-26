'''This includes implementation of Canny's Edge detection method
by default the lower is set to lowest 5% of the values and
upper is set to highest 5% of the values
'''

import cv2
import numpy as np
# matplotlib is imported during development phase
#import matplotlib.pyplot as plt

def filter_image(input_vector, lower=np.nan, upper=np.nan):
    print "Executing Phase 2: Edge Detection using Canny's Algorithm"
    input_vector = input_vector * 255.0 / np.max(input_vector)
    input_vector = np.uint8(input_vector)
    if np.isnan(lower) and np.isnan(upper):
        lower = np.percentile(input_vector, 5)
        upper = np.percentile(input_vector, 95)
    result = cv2.Canny(input_vector, lower, upper)
# Use the below functions to see how the output is coming
#    plt.imshow(result)
#    plt.show()
    return result
