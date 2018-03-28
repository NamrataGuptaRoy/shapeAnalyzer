'''This function implements PCA algorithm and produces the final plot'''

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def show_plot(value, title, similarity, filenames=[]):
    print "Executing Phase 4: Applying dimensionality reduciton using PCA"
    small = PCA(n_components=2).fit_transform(similarity)
    print "Executing Phase 5: Plotting similarity in 2-D graph"
    fig, ax = plt.subplots()
    ax.scatter(small[:,0], small[:, 1])
    if filenames != []:
        N = len(filenames)
        for i in xrange(N):
            ax.annotate(filenames[i].split('/')[1], (small[i][0], small[i][1]))
    plt.title(title)
    plt.show(block=value)
