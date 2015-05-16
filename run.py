# -*- coding: utf-8 -*-

"""\
© Copyright 2015. Joon Hyuk Yang.
Sociology 161. All rights reserved.

"""
from visualize import *
from cascade_model import *
from user import *
from time import time

# Global Variables
Q = 3
ERDOS_RENYI_P = 0.0125

# Desired number of users to influence in each group
N_CELEB = 5
N_FREQ = 10
N_RARE = 0
N_EAGER = 0
N_NORM = 30

###############################################################################

if __name__ == "__main__":
	starttime = time()
	pop = populate(CELEB, FREQ, RARE, EAGER, NORM)
	#rg = RandomGraph(pop)
	#b = rg.erdos_renyi_alg(ERDOS_RENYI_P)
#	fbg1 = FacebookGraph(pop)
#	fbg2 = FacebookGraph(pop)
#	fbg3 = FacebookGraph(pop)
#	fbg4 = FacebookGraph(pop)
#	fbg5 = FacebookGraph(pop)
#	fbg1.preferential_attachment(Q)
#	fbg2.preferential_attachment(Q)
#	fbg3.preferential_attachment(Q)
#	fbg4.preferential_attachment(Q)
#	fbg5.preferential_attachment(Q)
	# returns a list with binary results 1 for positive, 0 for no effect
	#fbg1.run_cascade([N_CELEB, N_FREQ, N_RARE, N_EAGER, N_NORM])
#	fbg1.run_cascade([2,0,0,0,0])
#	fbg2.run_cascade([0,20,0,0,0])
#	fbg3.run_cascade([2,10,0,10,0])
#	fbg4.run_cascade([0,0,0,15,0])
#	fbg5.run_cascade([0,0,0,0,30])
	for i in xrange(10):
		for j in xrange(3):
			fbg = FacebookGraph(pop)
			fbg.preferential_attachment(Q)
			print "celeb: {} freq: {} rare: {} eager: {} norm: {}".format(j,
														 25-5*j, 3, i, 30-2*i)
			fbg.run_cascade([j, 25-5*j, 3, i, 30-2*i])
	
	#draw_facebook_graph(friend_relations)
