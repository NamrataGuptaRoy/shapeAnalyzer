'''This is the driver function'''

from shapeAnalysisProject.input.x_ray import read_image
from shapeAnalysisProject.image_filtering.x_ray.Sobel import filter_image
from shapeAnalysisProject.shape_matching.Hu_moments import similarity as similarity_Hu
from shapeAnalysisProject.shape_matching.hausdorff import similarity as similarity_Hausdorff
from shapeAnalysisProject.dimension_reduction.PCA import show_plot as show_plot_PCA
from shapeAnalysisProject.dimension_reduction.TSNE import show_plot as show_plot_TSNE
from shapeAnalysisProject.statistics.statistics import variance
import glob
import sys
import numpy as np
import matplotlib.pyplot as plt

try:
    print sys.argv[1]
    filenames = glob.glob(sys.argv[1]+"/*.fits")
    print filenames
except:
    print "Correct Way of execution: python main.py <input_directory>"
    exit(1)

sim = [0, 0]
for filename in filenames:
    print "For File: ", filename.split('/')[1]
    sim[0] = similarity_Hu(filter_image(read_image(filename)))
    sim[1] = similarity_Hausdorff(filter_image(read_image(filename)))
sim = [np.array(sim[0]),np.array(sim[1])]
for t in xrange(2):
    similarity = sim[t]
    var = variance(similarity, filenames)
    if t==0:
        print "The top most common shapes using Hu_moments are:"
    else:
        print "The top most common shapes using Hausdorff distance are:"
    for val in var:
        print val[1]
    print "The similarity matrix is: "
    print similarity
    for i in xrange(3): # Print top 3 most common images
        plt.imshow(read_image(var[i][1]))
        if t==0:
            plt.title("Using Hu_moments:\n Top "+str(i+1)+" image: "+var[i][1].split('/')[1])
        else:
            plt.title("Using Haussdorff distance:\n Top "+str(i+1)+" image: "+var[i][1].split('/')[1])
        plt.show()
show_plot_PCA(sim[0], filenames, False, "Hu_moments and PCA")
show_plot_TSNE(sim[0], filenames, False, "Hu_moments and TSNE")
show_plot_PCA(sim[1], filenames, False, "Hausdorff Distance and PCA")
show_plot_TSNE(sim[1], filenames, True, "Hausdorff Distance and TSNE")
