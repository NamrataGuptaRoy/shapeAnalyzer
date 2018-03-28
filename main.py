'''This is the driver function'''

from shapeAnalysisProject.input.x_ray import read_image
from shapeAnalysisProject.image_filtering.x_ray.Sobel import filter_image
from shapeAnalysisProject.shape_matching.Hu_moments import similarity
from shapeAnalysisProject.shape_matching.hausdorff import similarity_hausdorff
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
        sim1 = similarity(filter_image(read_image(filename)))
        sim2 = similarity_hausdorff(filter_image(read_image(filename)))
    for i in sim1:
        for j in i:
            print j,'||\t',
        print
    show_plot(False, "Hu_moments", sim1, filenames)
    for i in sim2:
        for j in i:
            print j,'||\t',
        print
    show_plot(True, "Hausdorff Distance", sim2, filenames)
except:
    print "Correct Way of execution: python main.py <input_directory>"

