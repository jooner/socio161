# -*- coding: utf-8 -*-

"""\
© Copyright 2015. Joon Hyuk Yang.
Sociology 161. All rights reserved.

"""
from user import *
from cascade_model import *

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Celebrities: White 50
# Frequent Users: Blue 35
# Rare Users: Red 20
# Eager Users: Green 35
# Normal Users: Black 28

###############################################################################

def draw_facebook_graph(rxn_dict):

  all_edges = []
  for usr in rxn_dict:
    for friend in rxn_dict[usr]:
      all_edges.append((usr, friend))
  G = nx.path_graph(200)
  pos = nx.random_layout(G)
  nx.draw_networkx_nodes(G,pos, nodelist=[i for i in range(CELEB)],
                                node_color='w',
                                node_size=50)
  A = CELEB + FREQ
  nx.draw_networkx_nodes(G,pos, nodelist=[i for i in range(CELEB, A)],
                                node_color='b',
                                node_size=35)
  B = A + RARE
  nx.draw_networkx_nodes(G,pos, nodelist=[i for i in range(A, B)],
                                node_color='r',
                                node_size=20)
  C = B + EAGER
  nx.draw_networkx_nodes(G,pos, nodelist=[i for i in range(B, C)],
                                node_color='g',
                                node_size=35)
  D = C + NORM
  nx.draw_networkx_nodes(G,pos, nodelist=[i for i in range(C, D)],
                                node_color='k',
                                node_size=28)
  nx.draw_networkx_edges(G,pos,
                       edgelist=all_edges,
                       width=0.3, edge_color='b')
  nx.draw_networkx_labels(G, pos, {})
  plt.show()


def plot_degree_distr(degrees):
  x = np.arange(min(degrees), max(degrees) + 1)
  plt.xlabel('Degree')
  plt.ylabel('Fraction of users with degree')
  plt.plot(x, poisson.pmf(x, np.mean(degrees)), color='red')
  plt.hist(degrees, normed=1, bins=x, color='green')
  show()
