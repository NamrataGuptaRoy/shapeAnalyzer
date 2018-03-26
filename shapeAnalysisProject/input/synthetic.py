''''This file will just read synthetic data and return them in matrix
form to be used for filteration purpoose using techniques like
Canny's Edge Detection Algorithm
'''

import cv2

def read_image(filename):
    if filename == '':
        print "Could not find any filename in\
            shapeAnalysisProject.input.synthetic.py module"
        return []
    elif '.fits' in filename:
        print "The input file is of FITS type but the input module used is for\
            RBG i.e. shapeAnalysisProject.input.synthetic.py"
        return []
    img = cv2.imread(filename)
    return img
