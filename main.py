'''This is the driver function'''

from shapeAnalysisProject.input.x_ray import read_image
from shapeAnalysisProject.image_filtering.x_ray.Sobel import filter_image
from shapeAnalysisProject.shape_matching.Hu_moments import similarity
from shapeAnalysisProject.dimension_reduction.PCA import show_plot
import glob
import sys

try:
    print sys.argv[1]
    filenames = glob.glob(sys.argv[1]+"/*.fits")
    print filenames
    sim = []
    for filename in filenames:
        print "For File: ", filename.split('/')[1]
        sim = similarity(filter_image(read_image(filename)))
    for i in sim:
        for j in i:
            print j,'||\t',
        print
    show_plot(sim, filenames)
except:
    print "Correct Way of execution: python main.py <input_directory>"

