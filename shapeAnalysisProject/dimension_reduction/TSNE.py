from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def show_plot(similarity, filenames=[], value=True, title=""):
    print "Executing Phase 4: Applying dimensionality reduction using TSNE"
    small = TSNE(n_components=2).fit_transform(similarity)
    print "Executing Phase 5: Plotting similarity in 2-D graph"
    fig, ax = plt.subplots()
    ax.scatter(small[:,0], small[:, 1])
    if filenames != []:
        N = len(filenames)
        for i in xrange(N):
            ax.annotate(filenames[i].split('/')[1], (small[i][0], small[i][1]))
    plt.title(title)
    plt.tight_layout(rect=[0,0,1,1])
    plt.show(block=value)