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

def graph(log):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    for specie in log.keys():
        plt.plot(log[specie], label=specie)

    plt.legend(loc='center left', bbox_to_anchor=(1, .5), fancybox=True)
    ax.set(xlabel='Time', ylabel='Concentration')
    ax.grid()
    plt.show()

def crn(reactions, species, volume, time, deterministic):
    log = {n: [] for n in species.keys()}
    while (time > 0):
        for i in reactions:
            rate = get_reaction_rate(i, species, volume)
            if rate != -1:
                if deterministic:
                    do_reaction(i, 1/rate, species)
                else:
                    do_reaction(i, np.random.poisson(1/rate), species)

        for specie in species.keys():
            log[specie].append(species[specie])
        time -= 1
    print(species)
    graph(log)
