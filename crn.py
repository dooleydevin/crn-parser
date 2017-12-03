import random
import math
import time
import numpy as np

example = "parity"

# oscillator
if (example == "oscillator"):
  reactions = [[{'A': 1, 'B': 1}, {'B': 2}, 1], [{'B': 1, 'C': 1}, {'C': 2}, 1], [{'C': 1, 'A': 1}, {'A': 2}, 1]]
  species = {'A': 100, 'B': 100, 'C': 100}
  rates = [1, 1, 1]

# parity
if (example == "parity"):
  reactions = [[{'A': 2}, {}, .01]]
  species = {'A': 101}
  rates = [1]

volume = 1000
log = []
time = 100000

def do_step():
    global reactions, rates, species, volume, log, tau
    update_rates()
    for i in range(0, len(rates)):
        rate = rates[i]
        if rate != -1:
            do_reaction(reactions[i], np.random.poisson(1/rates[i]))
    log.append(species)

def do_reaction(reaction, n):
    global species
    for x in reaction[0].keys():
        species[x] -= n * reaction[0][x]
    for y in reaction[1].keys():
        species[y] += n * reaction[1][y]

def update_rates():
    global species, reactions, rates, volume
    for i in range(0, len(reactions)):
        reaction = reactions[i]
        rates[i] = reaction[2] 
        for y in reaction[0].keys():
            for j in range(0, reaction[0][y]):
                if species[y] - j > 0:
                    rates[i] = float(rates[i]) / (species[y] - j)
                    rates[i] *= volume
                else:
                    rates[i] = -1

while (time > 0):
    do_step()
    time -= 1

print(species)
# log is now full of species - graph it somehow
