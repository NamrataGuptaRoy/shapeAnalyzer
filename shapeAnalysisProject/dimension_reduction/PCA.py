'''This function implements PCA algorithm and produces the final plot'''

from sklearn.decomposition import PCA
from find_accuracy import evaluate_performance
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def show_plot(similarity, filenames=[], value=True, title=""):
    print "Executing Phase 4: Applying dimensionality reduction using PCA"
    small = PCA(n_components=2).fit_transform(similarity)
    error = evaluate_performance(small, similarity)
    print "Executing Phase 5: Plotting similarity in 2-D graph"
    fig, ax = plt.subplots()
    ax.scatter(small[:,0], small[:, 1],color=error)
    if filenames != []:
        N = len(filenames)
        for i in xrange(N):
            ax.annotate(filenames[i].split('/')[1], (small[i][0], small[i][1]))
    plt.title(title)
    red_patch = mpatches.Patch(color='red', label='These points are wrongly plotted')
    blue_patch = mpatches.Patch(color='blue', label='These points are correctly plotted')
    plt.legend(handles=[red_patch, blue_patch])
    plt.show(block=value)
