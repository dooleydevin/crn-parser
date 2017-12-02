import random
import math
import time
import numpy as np

do_step(reactions, rates, species, volume, log):
  update_rates(species, reactions, rates, volume):
  for i in xrange(0, len(rates)):
	  do_reaction(reactions[i], species, np.random.poisson(1/rates[i]))
  log.append(species)

do_reaction(reaction, species, n):
  for x in reaction[0].keys():
	species[x] -= n * reaction[0][x]
  for y in reaction[1].keys():
	species[x] += n * reaction[1][x]

update_rates(species, reactions, rates, volume):
  for i in xrange(0, len(reactions)):
	reaction = reactions[i]
	rates[i] = reaction[2] 
	for y in reaction[0].keys():
	  for j in xrange(0, reaction[0][y]):
		rates[i] *= species[y] - j
		rates[i] /= volume


