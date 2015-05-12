# -*- coding: utf-8 -*-

"""\
© Copyright 2015. Joon Hyuk Yang.
Sociology 161. All rights reserved.

"""
from user import *
from pylab import show
from scipy.stats import poisson
from random import random, shuffle
from time import time

import numpy as np

# Global Variables
CELEB_CLIQUE = 3
TOTAL_USERS = 200
RUNTIME_CAP = 5 # in seconds 

###############################################################################

class RandomGraph:

  def __init__(self, population):
    # list of User objects
    self.users = population
    self.pop = len(population)
    self.relations = {i:[] for i in xrange(self.pop)}
    self.degrees = [0 for i in xrange(self.pop)]

  def befriend(self, usr1, usr2):
    # Making sure that both nodes record each other
    self.relations[usr1].append(usr2)
    self.relations[usr2].append(usr1)
    self.degrees[usr1] += 1
    self.degrees[usr2] += 1

  def erdos_renyi_alg(self, p):
    """Naive implementation of random graph with uniform users"""
    for i in xrange(self.pop):
      for j in xrange(i + 1, self.pop):
        if random() < p:
          self.befriend(i, j)
    return self.relations


class FacebookGraph(RandomGraph):

  def __init__(self, population):
    RandomGraph.__init__(self, population)

  def preferential_attachment(self, q):

    def choose_edge(size, degrees):
      """Form q edges with existing vertices"""
      prob = map(lambda x: x / float(sum(degrees)), degrees)
      return np.random.choice(len(degrees), size=size, p=prob)

    def check_then_add(usr1, usr2):
      if usr1 != usr2 and (usr2 not in self.relations[usr1]) and \
      len(self.relations[usr1]) < self.users[usr1].friends and \
      len(self.relations[usr2]) < self.users[usr2].friends:
        self.befriend(usr1, usr2)

    def form_connected_world():
      # first celebrities are friends with one another
      for celeb1 in xrange(CELEB_CLIQUE):
        for celeb2 in xrange(celeb1 + 1, CELEB_CLIQUE):
          self.befriend(celeb1, celeb2)
      # shuffling the order of users
      usr_idx = [i for i in xrange(TOTAL_USERS)]
      shuffle(usr_idx)
      # what the goal degrees is supposed to be
      goal_degrees = [self.users[i].friends for i in xrange(TOTAL_USERS)]
      start_time = time()
      # run until we find the desired assignment, or if it is impossible
      # in a reasonable time, then cap the running time
      while (goal_degrees != self.degrees) and \
            (time() - start_time < RUNTIME_CAP) :
        # repeat PA until we reach goal friends for each user
        for usr1 in filter(lambda x: self.users[x].friends != \
                           len(self.relations[x]), usr_idx):
          rand_metric = random()
          # 10% of the time, randomly select possible edges
          if rand_metric < 0.1:
            for usr2 in np.random.choice(len(self.degrees), q):
              check_then_add(usr1, usr2)
          # 90% PA algorithm
          else:
            for usr2 in choose_edge(q, self.degrees):
              check_then_add(usr1, usr2)
    form_connected_world()
    return self.relations
