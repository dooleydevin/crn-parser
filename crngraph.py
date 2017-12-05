import matplotlib.pyplot as plt

def graph(log):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    for specie in log.keys():
        plt.plot(log[specie], label=specie)

    plt.legend(loc='center left', bbox_to_anchor=(1, .5), fancybox=True)
    ax.set(xlabel='Time', ylabel='Concentration')
    ax.grid()
    plt.show()
