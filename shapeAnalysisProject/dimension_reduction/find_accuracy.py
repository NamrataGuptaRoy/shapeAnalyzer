'''This module identifies points that do not satisfy the invariant
mentioned in the similarity matrix. Please refer the research paper'''

import math
def distance(point_1, point_2):
	return math.pow(math.pow(point_1[0] - point_2[0], 2) + math.pow(point_1[1] -
			point_2[1], 2), 0.5)

def evaluate_performance(small, similarity):
	N = similarity.shape[0]
	proximity_N = [] # proximity matrix in N-dimension
	for i in xrange(N):
		proximity_N.append([])
		for j in xrange(N):
			proximity_N[i].append([similarity[i][j], j])
		proximity_N[i].sort()
	proximity_2 = [] # proximity matrix in 2-dimension
	for i in xrange(N):
		proximity_2.append([])
		for j in xrange(N):
			proximity_2[i].append([distance(small[i], small[j]), j])
		proximity_2[i].sort()

	error = ['blue' for i in xrange(N)] # this stores points wrongly plotted in 2D
	for i in xrange(N):
		for j in xrange(N):
			if proximity_N[i][j][1] != proximity_2[i][j][1]:
				error[j] = 'red'
	return error
