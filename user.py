# -*- coding: utf-8 -*-

"""\
© Copyright 2015. Joon Hyuk Yang.
Sociology 161. All rights reserved.

"""
from random import randint

# Global Variables
BASE_FRIENDS = 5 #15 # dec. by 90%
MAX_FRIENDS = 50 #0 # dec. by 90%

CELEB = 5
FREQ = 50
RARE = 50
EAGER = 25
NORM = 70

###############################################################################


class User(object):
  """\
  This User class defines the attributes for any given user i:

    :param _id: unique id number to identify each user
    :param friends: how many edges user i has with other users
    :param influence: how much weight each user has on others
    :param responsive: how willing each user is to respond to the ad

  NB: responsive can be thought of as how likely a user, after having seen
      an ad, will actively post about it and signal it to other users.

  """
  def __init__(self, _id, friends, influence, responsive):
    self._id = _id
    self.friends = friends
    self.influence = influence
    self.responsive = responsive

  def __str__(self):
    return "{} ID\n{} Friends\n{} Influence\n{} Responsive\
           ".format(self._id, self.friends, self.influence, self.responsive)


class FacebookUser(User):
  def __init__(self):
    

def spec(idx, spec_type):
  """\
  Generic specification handler for different user types providing
  approrpiate friend, influence, and responsiveness metrics for
  each user id.

  Friend base is based off Facebook but lowered by X percent specified
  in Global Variable section.

  """
  if spec_type == 'celeb':
    f = randint(30, MAX_FRIENDS)
    i = randint(60, 75) # highly influential
    r = randint(0, 10) # low response to ads
  elif spec_type == 'freq':
    f = randint(BASE_FRIENDS, 20)
    i = randint(20, 50) # medium influence
    r = randint(35, 60) # medium-high response to ads
  elif spec_type == 'rare':
    f = randint(BASE_FRIENDS, 8)
    i = randint(1, 20) # low influence
    r = randint(5, 25) # low response to ads
  elif spec_type == 'eager':
    f = randint(BASE_FRIENDS, 25)
    i = randint(20, 50) # medium influence
    r = randint(50, 80) # very high response to ads
  elif spec_type == 'norm':
    f = randint(BASE_FRIENDS, 15)
    i = randint(10, 30) # medium-low influence
    r = randint(10, 30) # medium response to ads
  else:
    raise ValueError("Unspecified Type {}".format(spec_type))
  return idx, f, i, r

def populate(n_celeb, n_freq, n_rare, n_eager, n_norm):
  """\
  Given how many celebrities, frequent users, rare users,
  eager users, and normal users, return a list of User objects
  in the population.

  """
  celeb, freq, rare, eager, norm = [], [], [], [], []
  for i in xrange(n_celeb):
    _id, _f, _i, _r = spec(i, 'celeb')
    celeb.append(User(_id, _f, _i, _r))
  for i in xrange(n_freq):
    _id, _f, _i, _r = spec(i + n_celeb, 'freq')
    freq.append(User(_id, _f, _i, _r))
  for i in xrange(n_rare):
    _id, _f, _i, _r = spec(i + n_celeb + n_freq, 'rare')
    rare.append(User(_id, _f, _i, _r))
  for i in xrange(n_eager):
    _id, _f, _i, _r = spec(i + n_celeb + n_freq + n_rare, 'eager')
    eager.append(User(_id, _f, _i, _r))
  for i in xrange(n_norm):
    _id, _f, _i, _r = spec(i + n_celeb + n_freq + n_rare + n_eager, 'norm')
    norm.append(User(_id, _f, _i, _r))
  return celeb + freq + rare + eager + norm
