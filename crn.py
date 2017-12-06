import random
import math
import time
import numpy as np

from crngraph import graph

example = "oscillator"

# oscillator
if (example == "oscillator"):
    reactions = [[{'A': 1, 'B': 1}, {'B': 2}, 0.1],
               [{'B': 1, 'C': 1}, {'C': 2}, 0.1],
               [{'C': 1, 'A': 1}, {'A': 2}, 0.1]]
    species = {'A': 130, 'B': 100, 'C': 70}

# parity
if (example == "parity"):
    reactions = [[{'A': 2}, {}, .01]]
    species = {'A': 101}
    rates = [1]

volume = 500
log = {n: [] for n in species.keys()} 
time = 5000

def do_step():
    global reactions, rates, species, volume, log
    for i in reactions:
        rate = get_reaction_rate(i, species)
        if rate != -1:
            do_reaction(i, np.random.poisson(1/rate), species)

    for specie in species.keys():
        log[specie].append(species[specie])

def do_reaction(reaction, n, species):
    for x in reaction[0].keys():
        species[x] -= n * reaction[0][x]
    for y in reaction[1].keys():
        species[y] += n * reaction[1][y]

def get_reaction_rate(reaction, species):
    rate = reaction[2]
    for y in reaction[0]:
        for j in range(reaction[0][y]):
            if species[y] - j > 0:
                rate *= volume / (species[y] - j)
            else:
                return -1
    return rate

while (time > 0):
    do_step()
    time -= 1

graph(log)
