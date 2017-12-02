import random
import math
import time
import numpy as np

reactions = []
rates = []
species = dict()
volume = 1
log = []
time = 10000

def do_step():
  global reactions, rates, species, volume, log, tau
  update_rates()
  for i in xrange(0, len(rates)):
	  do_reaction(np.random.poisson(1/rates[i]))
  log.append(species)

def do_reaction(n):
  global reactions, species
  for x in reaction[0].keys():
	species[x] -= n * reaction[0][x]
  for y in reaction[1].keys():
	species[x] += n * reaction[1][x]

def update_rates():
  global species, reactions, rates, volume
  for i in xrange(0, len(reactions)):
	reaction = reactions[i]
	rates[i] = reaction[2] 
	for y in reaction[0].keys():
	  for j in xrange(0, reaction[0][y]):
		rates[i] *= species[y] - j
		rates[i] /= volume

while (time > 0):
  do_step()
  time -= 1

# log is now full of species - graph it somehow
