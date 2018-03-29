'''This function uses Hu-moments to compute the shape similarity of 2 grayscale images'''

import cv2

def similarity_Hu(new_image, images=[], similarity=[]):
    print "Executing Phase 3: Calculating similarity of shapes using Hu-moments"
    N = len(images)
    for i in xrange(N):
        similarity[i].append(cv2.matchShapes(images[i], new_image, 1, 0.0))
    similarity.append([])
    for i in xrange(N):
        similarity[N].append(similarity[i][N])
    similarity[N].append(0.0)
    images.append(new_image)
    return similarity
