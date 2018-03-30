from scipy.spatial.distance import directed_hausdorff

def similarity(new_image, images=[], similarity=[]):
    print "Executing Phase 3: Calculating similarity of shapes using Hausdorff distance"
    N = len(images)
    for i in xrange(N):
        similarity[i].append(max(directed_hausdorff(images[i], new_image)[0],directed_hausdorff(new_image,images[i])[0]))
    similarity.append([])
    for i in xrange(N):
        similarity[N].append(similarity[i][N])
    similarity[N].append(0.0)
    images.append(new_image)
    return similarity
