'''This filw will just read X_ray data present in FITS format and return them
in matrix form to be used for image filtering algorithms like
Canny's Edge Detection Algorithm
'''

from astropy.io import fits
import numpy as np

def read_image(filename):
    print "Executing Phase 1: reading data from FITS file"
    if filename == '':
        print "No file found while parsing"
        return []
    elif '.fits' not in filename:
        print "The file is not of FITS format and the input module used is \
            for that of the FITS files"
        return []
    try:
        hdulist = fits.getdata(filename)
        return np.array(hdulist)
    except:
        print "No data found in file: ", filename
        return []
