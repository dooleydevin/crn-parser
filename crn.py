import random
import math
import time
import numpy as np

import matplotlib.pyplot as plt

def do_reaction(reaction, n, species):
    for x in reaction[0].keys():
        species[x] -= n * reaction[0][x]
    for y in reaction[1].keys():
        species[y] += n * reaction[1][y]

def get_reaction_rate(reaction, species, volume):
    rate = reaction[2]
    for y in reaction[0]:
        for j in range(reaction[0][y]):
            if species[y] - j > 0:
                rate *= volume / (species[y] - j)
            else:
                return -1
    return rate

def graph(t, log):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    for species in log.keys():
        plt.plot(t, log[species], label=species)

    plt.legend(loc='center left', bbox_to_anchor=(1, .5), fancybox=True)
    ax.set(xlabel='Time', ylabel='Concentration')
    ax.grid()
    plt.show()

def crn(reactions, species, volume, time, dt, deterministic):
    log = {n: [] for n in species.keys()}
    t = np.arange(0, time, dt)
    for tick in t:
        for i in reactions:
            rate = get_reaction_rate(i, species, volume)
            if rate != -1:
                if deterministic:
                    do_reaction(i, dt/rate, species)
                else:
                    do_reaction(i, np.random.poisson(dt/rate), species)

        for specie in species.keys():
            log[specie].append(species[specie])
    print(species)
    graph(t, log)
