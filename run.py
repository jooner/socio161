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

###############################################################################

if __name__ == "__main__":
	starttime = time()
	pop = populate(CELEB, FREQ, RARE, EAGER, NORM)
	rg = RandomGraph(pop)
	#b = rg.erdos_renyi_alg(ERDOS_RENYI_P)
	fbg = FacebookGraph(pop)
	a = fbg.preferential_attachment(Q)
	draw_facebook_graph(a)
