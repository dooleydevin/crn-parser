import matplotlib.pyplot as plt

def graph(log):
    fig, ax = plt.subplots()

    for specie in log.keys():
        plt.plot(log[specie])

    ax.set(xlabel='Time', ylabel='Concentration')
    ax.grid()
    plt.show()
