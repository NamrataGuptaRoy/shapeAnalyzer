import numpy as np

def variance(similarity, filenames):
    sim_var = np.var(similarity, axis=0)
    variance = []
    N = similarity.shape[0]
    for i in xrange(N):
        variance.append([sim_var[i], filenames[i]])
    variance.sort()
    return variance
